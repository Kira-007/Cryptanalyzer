# app.py
import os
import traceback
import json
from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import io
import sys
from contextlib import redirect_stdout
from config import get_config

# Import your modules
# Make sure modules/ is a package (contains __init__.py) OR adjust Python path
# This code assumes your uploaded files are in modules/ (aes.py, rsa.py, hashAttacker.py)
try:
    from modules import aes as aes_module
    from modules import rsa as rsa_module
    from modules import hashAttacker as hash_module
except Exception as e:
    # If modules is not a package, try to import via file path fallback
    import importlib.util
    def load_module_from_path(name, path):
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    base = os.path.join(os.path.dirname(__file__), "modules")
    aes_module = load_module_from_path("aes", os.path.join(base, "aes.py"))
    rsa_module = load_module_from_path("rsa", os.path.join(base, "rsa.py"))
    hash_module = load_module_from_path("hashAttacker", os.path.join(base, "hashAttacker.py"))

# Load configuration
config = get_config(os.environ.get('FLASK_ENV', 'development'))

# Create uploads folder
os.makedirs(config.UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_object(config)

# ---------- Helpers ----------
def run_and_capture(func, *args, **kwargs):
    """Run a function that prints to stdout and capture printed output."""
    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            result = func(*args, **kwargs)
    except Exception as e:
        tb = traceback.format_exc()
        return {"success": False, "error": str(e), "traceback": tb, "output": buf.getvalue()}
    return {"success": True, "result": result, "output": buf.getvalue()}

# ---------- Routes: Web UI ----------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aes")
def aes_page():
    return render_template("aes.html")
@app.route("/ecc")
def ecc_page():
    return render_template("ecc.html")
@app.route("/rsa")
def rsa_page():
    return render_template("rsa.html")

@app.route("/hash")
def hash_page():
    return render_template("hash.html")

@app.route("/encode")
def encode_page():
    return render_template("encode.html")

# ---------- Routes: Static uploads (for wordlists etc.) ----------
@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

# ---------- API Endpoints ----------
@app.route("/api/aes/cpa", methods=["POST"])
def api_aes_cpa():
    """
    POST JSON: { "server": "<server-string>" }
    WARNING: aes.cpa expects to spawn a process via `process(server)` (pwntools).
    This endpoint will try to call aes_module.cpa(server) and capture output.
    """
    data = request.get_json() or {}
    server = data.get("server", "")
    if not server:
        return jsonify({"success": False, "error": "Missing 'server' parameter"}), 400

    # Call cpa and capture prints (may block or fail if pwntools/process not available)
    out = run_and_capture(aes_module.cpa, server)
    return jsonify(out)

@app.route("/api/rsa/pem", methods=["POST"])
def api_rsa_pem():
    """
    POST form-data: file field 'public'
    Returns the printed output and (if created) private.pem location.
    """
    if 'public' not in request.files:
        return jsonify({"success": False, "error": "No 'public' file uploaded"}), 400
    f = request.files['public']
    filename = secure_filename(f.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    f.save(path)
    # call rsa_module.rsa_pem(path), capture stdout
    out = run_and_capture(rsa_module.rsa_pem, path)
    # if private.pem saved in cwd, provide link if exists
    priv_path = os.path.join(os.getcwd(), "private.pem")
    if os.path.exists(priv_path):
        out['private_pem'] = "/private.pem"
    return jsonify(out)

@app.route("/private.pem")
def download_private_pem():
    p = os.path.join(os.getcwd(), "private.pem")
    if os.path.exists(p):
        return send_from_directory(os.getcwd(), "private.pem", as_attachment=True)
    return jsonify({"success": False, "error": "private.pem not found"}), 404

@app.route("/api/rsa/factor", methods=["POST"])
def api_rsa_factor():
    """
    POST JSON: { "n": <int>, "e": <int>, "c": <int>, "p": <int>?, "q": <int>? }
    Supports the same cases as your CLI. Returns printed output and function result if any.
    """
    data = request.get_json() or {}
    n = data.get("n")
    e = data.get("e")
    c = data.get("c")
    p = data.get("p")
    q = data.get("q")

    # Try the combinations your CLI expected (wrap to call rsa_module.rsa_fact / rsa_module.rsa etc.)
    try:
        if n and e and c:
            out = run_and_capture(rsa_module.rsa_fact, n, e, c)
        elif p and q and e and c:
            out = run_and_capture(rsa_module.rsa, p, q, e, c)
        elif e == 3 and c:
            out = run_and_capture(rsa_module.rsa_e, c, e)
        else:
            return jsonify({"success": False, "error": "Insufficient or incorrect RSA parameters"}), 400
        return jsonify(out)
    except Exception as ex:
        tb = traceback.format_exc()
        return jsonify({"success": False, "error": str(ex), "traceback": tb}), 500

# ----- Hash tools -----
@app.route("/api/hash/crack", methods=["POST"])
def api_hash_crack():
    """Form-data: wordlist (file) OR wordlist_path; and fields 'hash' and 'algo'"""
    # Accept either file upload or a previously uploaded path
    target_hash = request.form.get('hash') or (request.json and request.json.get('hash'))
    algo = request.form.get('algo') or (request.json and request.json.get('algo'))
    # wordlist: either upload or path
    if 'wordlist' in request.files:
        wf = request.files['wordlist']
        wfname = secure_filename(wf.filename)
        wfpath = os.path.join(app.config['UPLOAD_FOLDER'], wfname)
        wf.save(wfpath)
    else:
        wfpath = request.form.get('wordlist_path') or (request.json and request.json.get('wordlist_path'))
    if not (target_hash and algo and wfpath):
        return jsonify({"success": False, "error": "Required: hash, algo, and wordlist (upload or path)"}), 400

    class Args: pass
    args = Args()
    args.hash = target_hash
    args.algo = algo
    args.wordlist = wfpath
    out = run_and_capture(hash_module.crack_hash, args)
    return jsonify(out)

@app.route("/api/hash/rainbow-gen", methods=["POST"])
def api_rainbow_gen():
    """
    Form-data: wordlist (file) OR wordlist_path, algo, output filename
    """
    algo = request.form.get('algo')
    output = request.form.get('output') or "rainbow.json"
    if 'wordlist' in request.files:
        wf = request.files['wordlist']
        wfname = secure_filename(wf.filename)
        wfpath = os.path.join(app.config['UPLOAD_FOLDER'], wfname)
        wf.save(wfpath)
    else:
        wfname = request.form.get('wordlist_path')
        wfname = wfname if wfname else None
        wfname = wfname
        wfpath = wfname
    if not (algo and wfpath):
        return jsonify({"success": False, "error": "Required: algo and wordlist (upload or path)"}), 400

    class Args: pass
    args = Args()
    args.algo = algo
    args.wordlist = wfpath
    args.output = os.path.join(app.config['UPLOAD_FOLDER'], output)
    out = run_and_capture(hash_module.rainbow_generate, args)
    # Return download link if created
    if os.path.exists(args.output):
        out['rainbow_table'] = "/uploads/" + os.path.basename(args.output)
    return jsonify(out)

@app.route("/api/hash/rainbow-lookup", methods=["POST"])
def api_rainbow_lookup():
    hashv = request.form.get('hash') or (request.json and request.json.get('hash'))
    table = request.form.get('table_path') or (request.json and request.json.get('table'))
    if 'table' in request.files:
        tf = request.files['table']
        tname = secure_filename(tf.filename)
        tpath = os.path.join(app.config['UPLOAD_FOLDER'], tname)
        tf.save(tpath)
        table = tpath
    if not (hashv and table):
        return jsonify({"success": False, "error": "Required: hash and rainbow table (upload or path)"}), 400
    class Args: pass
    args = Args()
    args.hash = hashv
    args.table = table
    out = run_and_capture(hash_module.rainbow_lookup, args)
    return jsonify(out)

@app.route("/api/hash/hmac-brute", methods=["POST"])
def api_hmac_brute():
    hmac_hex = request.form.get('hmac') or (request.json and request.json.get('hmac'))
    msg = request.form.get('msg') or (request.json and request.json.get('msg'))
    algo = request.form.get('algo') or (request.json and request.json.get('algo'))
    if 'wordlist' in request.files:
        wf = request.files['wordlist']
        wfname = secure_filename(wf.filename)
        wfpath = os.path.join(app.config['UPLOAD_FOLDER'], wfname)
        wf.save(wfpath)
    else:
        wfpath = request.form.get('wordlist_path') or (request.json and request.json.get('wordlist'))
    if not (hmac_hex and msg and algo and wfpath):
        return jsonify({"success": False, "error": "Required: hmac, msg, algo, and wordlist (upload or path)"}), 400
    class Args: pass
    args = Args()
    args.hmac = hmac_hex
    args.msg = msg
    args.algo = algo
    args.wordlist = wfpath
    out = run_and_capture(hash_module.hmac_brute, args)
    return jsonify(out)

@app.route("/api/hash/birthday", methods=["POST"])
def api_birthday():
    algo = request.json.get('algo') if request.json else request.form.get('algo')
    length = int(request.json.get('length', 8)) if request.json else int(request.form.get('length', 8))
    if not algo:
        return jsonify({"success": False, "error": "Required: algo"}), 400
    class Args: pass
    args = Args()
    args.algo = algo
    args.length = length
    out = run_and_capture(hash_module.birthday_attack, args)
    return jsonify(out)

# ----- Encoding/Decoding endpoints (quick wrappers) -----
@app.route("/api/encode/<op>", methods=["POST"])
def api_encode(op):
    data = request.json or request.form or {}
    s = data.get('data')
    if s is None:
        return jsonify({"success": False, "error": "Missing 'data' parameter"}), 400
    try:
        if op == "base64-encode":
            res = hash_module.encode_base64(s)
        elif op == "base64-decode":
            res = hash_module.decode_base64(s)
        elif op == "hex-encode":
            res = hash_module.encode_hex(s)
        elif op == "hex-decode":
            res = hash_module.decode_hex(s)
        elif op == "url-encode":
            res = hash_module.encode_url(s)
        elif op == "url-decode":
            res = hash_module.decode_url(s)
        else:
            return jsonify({"success": False, "error": "Unknown op"}), 400
        return jsonify({"success": True, "result": res})
    except Exception as ex:
        tb = traceback.format_exc()
        return jsonify({"success": False, "error": str(ex), "traceback": tb}), 500

# ---------- Run ----------
if __name__ == "__main__":
    # run in debug for development only
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
