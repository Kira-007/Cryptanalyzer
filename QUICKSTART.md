# 🚀 Cryptanalyzer Web UI - Quick Start Guide

Get up and running in 3 easy steps!

## Prerequisites

- Python 3.7 or higher
- Internet connection (for dependency installation)

## Installation & Running

### Option 1: Automatic (Recommended)

#### On Linux/Mac:
```bash
./run_webui.sh
```

#### On Windows:
```cmd
run_webui.bat
```

The script will:
- ✅ Create a virtual environment
- ✅ Install all dependencies
- ✅ Start the web server
- ✅ Open at http://localhost:5000

### Option 2: Manual

```bash
# 1. Install dependencies
pip install -r reqirements.txt

# 2. Start the server
python app.py

# 3. Open browser
# Navigate to http://localhost:5000
```

## First Steps

### 1. Access the Dashboard
Open your browser and go to: **http://localhost:5000**

You'll see 4 main modules:
- 🔐 **AES Analyzer** - AES chosen plaintext attacks
- 🔑 **RSA Tools** - RSA factorization and decryption
- #️⃣ **Hash Attacks** - Dictionary attacks, rainbow tables, HMAC
- 🔤 **Encoding/Decoding** - Base64, Hex, URL encode/decode

### 2. Try Your First Attack - Hash Cracking

Let's crack a simple MD5 hash:

1. Click on **"Hash Attacks"**
2. In the "Dictionary / Brute-force Crack" section:
   - **Hash:** `5f4dcc3b5aa765d61d8327deb882cf99` (this is "password")
   - **Algo:** `md5`
   - **Wordlist:** Create a file with common passwords:
     ```bash
     echo -e "123456\npassword\nadmin\nletmein" > wordlist.txt
     ```
   - Upload the wordlist
3. Click **"Run Crack"**
4. Result: `[+] Found: password`

### 3. Try RSA Factorization

Test with a weak RSA key:

1. Click on **"RSA Tools"**
2. Scroll to "Factor / decrypt by params"
3. Enter test values:
   - **n:** `143` (= 11 × 13)
   - **e:** `7`
   - **c:** `2` (encrypted message)
4. Click **"Run"**
5. See the decrypted result!

### 4. Encoding/Decoding

Quick text transformations:

1. Click on **"Encoding / Decoding"**
2. Select operation: `Base64 Encode`
3. Enter text: `Hello, World!`
4. Click **"Run"**
5. Result: `SGVsbG8sIFdvcmxkIQ==`

## Common Use Cases

### Cracking Password Hashes

```bash
# 1. Get a wordlist (rockyou.txt is popular)
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

# 2. Use the Web UI:
- Go to Hash Attacks
- Enter your hash
- Select algorithm
- Upload rockyou.txt
- Click "Run Crack"
```

### RSA Key Recovery from PEM

```bash
# 1. Generate a test key
openssl genrsa -out private.pem 512
openssl rsa -in private.pem -pubout -out public.pem

# 2. Use the Web UI:
- Go to RSA Tools
- Upload public.pem
- Click "Upload & Extract"
- Download recovered private.pem
```

### Rainbow Table Attack

```bash
# 1. Generate rainbow table (one-time)
- Go to Hash Attacks → Rainbow Table Generate
- Select algorithm (e.g., sha256)
- Upload your wordlist
- Save as "rainbow_sha256.json"

# 2. Crack hashes instantly
- Go to Hash Attacks → Rainbow Table Lookup
- Enter hash
- Upload rainbow table
- Instant result!
```

## Troubleshooting

### "Port already in use"
If port 5000 is busy, edit `app.py`:
```python
app.run(host="0.0.0.0", port=5001, debug=True)  # Change to 5001
```

### "Module not found"
```bash
pip install -r reqirements.txt
```

### "Permission denied" (Linux/Mac)
```bash
chmod +x run_webui.sh
```

### Slow Performance
- Use smaller wordlists
- Pre-generate rainbow tables
- Ensure you have enough RAM

## Tips & Tricks

### 💡 Speed up hash cracking
Pre-generate rainbow tables for your common wordlists!

### 💡 Organize wordlists
Create a `data/wordlists/` folder:
```bash
mkdir -p data/wordlists
mv *.txt data/wordlists/
```

### 💡 Save results
Copy output from the result boxes and save to files for later reference.

### 💡 CLI Alternative
You can also use the command-line interface:
```bash
python main.py crack --hash <hash> --algo sha256 --wordlist wordlist.txt
```

## Security Warning ⚠️

**Important:**
- This tool is for **authorized security testing only**
- Do **NOT** expose the web server to the internet
- Default configuration binds to `0.0.0.0:5000` - **local use only**
- Add authentication for production use

## Next Steps

📖 **Read the full documentation:** `WEB_UI_README.md`

🔧 **Explore CLI options:** `python main.py --help`

🛠️ **Customize:** Edit templates in `templates/` folder

🎨 **Style changes:** Modify `static/css/style.css`

## Need Help?

- Check `WEB_UI_README.md` for detailed documentation
- Review `README.md` for general project info
- Examine example usage in the templates

---

**Happy Hacking! 🔐**

Remember: With great power comes great responsibility. Use ethically!
