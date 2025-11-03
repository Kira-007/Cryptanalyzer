# Cryptanalyzer Web UI Documentation

A Flask-based web interface for cryptographic analysis tools including RSA, AES, Hash attacks, and encoding/decoding utilities.

## 🚀 Quick Start

### Installation

1. **Install dependencies:**
```bash
pip install -r reqirements.txt
```

2. **Start the web server:**
```bash
python app.py
```

3. **Open your browser:**
Navigate to `http://localhost:5000`

## 📁 Project Structure

```
Cryptanalyzer/
├── app.py                  # Flask application
├── main.py                 # CLI interface
├── modules/                # Core cryptanalysis modules
│   ├── rsa.py             # RSA attacks
│   ├── aes.py             # AES attacks
│   └── hashAttacker.py    # Hash attacks & encoding
├── templates/              # HTML templates
│   ├── index.html         # Dashboard
│   ├── rsa.html           # RSA tools page
│   ├── aes.html           # AES tools page
│   ├── hash.html          # Hash attacks page
│   └── encode.html        # Encoding/decoding page
├── static/                 # Static assets
│   ├── css/
│   └── js/
└── uploads/               # Uploaded files (auto-created)
```

## 🛠️ Features

### 1. RSA Tools (`/rsa`)

#### Extract from PEM
- Upload RSA public key PEM file
- Automatically extracts `n` and `e`
- Factors `n` using FactorDB
- Generates private key (saved as `private.pem`)

**Usage:**
1. Click "Choose File" and select your public key PEM file
2. Click "Upload & Extract"
3. View results and download private key

#### RSA Factorization & Decryption
- **Case 1:** Given n, e, c → Factors n and decrypts
- **Case 2:** Given p, q, e, c → Direct decryption
- **Case 3:** Small exponent attack (e=3)

**Parameters:**
- `n`: RSA modulus
- `e`: Public exponent
- `c`: Ciphertext (as integer)
- `p`, `q`: Prime factors (optional)

### 2. AES Tools (`/aes`)

#### Chosen Plaintext Attack (CPA)
- Attacks AES encryption oracles
- Requires server running with oracle access
- Uses `pwntools` to interact with server

**Usage:**
1. Enter server string (e.g., `127.0.0.1:1337` or `./binary`)
2. Click "Run CPA"
3. Wait for attack to complete

**Note:** This requires a vulnerable AES oracle server to be running.

### 3. Hash Attacks (`/hash`)

#### Dictionary/Brute-force Crack
- Cracks hashes using wordlist
- Supports: MD5, SHA1, SHA256, SHA512, etc.

**Usage:**
1. Enter target hash
2. Select algorithm (e.g., `sha256`)
3. Upload wordlist file
4. Click "Run Crack"

#### Rainbow Table Generation
- Pre-computes hash values for wordlist
- Creates searchable JSON table
- Speeds up future hash lookups

**Usage:**
1. Select hash algorithm
2. Upload wordlist
3. Enter output filename
4. Click "Generate"
5. Download generated table

#### Rainbow Table Lookup
- Searches pre-computed rainbow table
- Instant hash cracking

**Usage:**
1. Enter hash to lookup
2. Upload rainbow table file
3. Click "Lookup"

#### HMAC Brute-force
- Cracks HMAC secret keys
- Uses wordlist attack

**Required Fields:**
- HMAC hex digest
- Original message
- Hash algorithm
- Wordlist file

#### Birthday Attack
- Demonstrates hash collision finding
- Generates random strings until collision

**Parameters:**
- Algorithm (e.g., `md5`)
- Random string length (default: 8)

### 4. Encoding/Decoding (`/encode`)

Quick encode/decode utilities:
- **Base64:** Encode/Decode
- **Hex:** Encode/Decode  
- **URL:** Encode/Decode

**Usage:**
1. Select operation from dropdown
2. Enter text in textarea
3. Click "Run"

## 🔌 API Endpoints

All API endpoints return JSON responses.

### RSA Endpoints

#### `POST /api/rsa/pem`
**Form-data:**
- `public`: Public key PEM file

**Response:**
```json
{
  "success": true,
  "output": "Extracted n: ...\nExtracted e: ...",
  "private_pem": "/private.pem"
}
```

#### `POST /api/rsa/factor`
**JSON:**
```json
{
  "n": 123456789,
  "e": 65537,
  "c": 987654321,
  "p": null,  // optional
  "q": null   // optional
}
```

### Hash Endpoints

#### `POST /api/hash/crack`
**Form-data:**
- `hash`: Target hash string
- `algo`: Algorithm name (md5, sha1, sha256, etc.)
- `wordlist`: Wordlist file

#### `POST /api/hash/rainbow-gen`
**Form-data:**
- `algo`: Algorithm name
- `wordlist`: Wordlist file
- `output`: Output filename (default: rainbow.json)

#### `POST /api/hash/rainbow-lookup`
**Form-data:**
- `hash`: Hash to lookup
- `table`: Rainbow table file OR `table_path`: path to table

#### `POST /api/hash/hmac-brute`
**Form-data:**
- `hmac`: HMAC hex digest
- `msg`: Message string
- `algo`: Hash algorithm
- `wordlist`: Wordlist file

#### `POST /api/hash/birthday`
**JSON:**
```json
{
  "algo": "md5",
  "length": 8
}
```

### Encoding Endpoints

#### `POST /api/encode/{operation}`
**Operations:** `base64-encode`, `base64-decode`, `hex-encode`, `hex-decode`, `url-encode`, `url-decode`

**JSON:**
```json
{
  "data": "text to encode/decode"
}
```

### AES Endpoints

#### `POST /api/aes/cpa`
**JSON:**
```json
{
  "server": "127.0.0.1:1337"
}
```

## 🔒 Security Considerations

⚠️ **WARNING:** This tool is intended for educational and authorized security testing only.

### Important Notes:
1. **Do NOT expose to internet** without proper authentication
2. **Local use only** - runs on `0.0.0.0:5000` by default
3. File uploads are saved to `uploads/` directory
4. Maximum upload size: 200 MB
5. All user inputs should be sanitized

### Secure Deployment (if needed):
```python
# app.py - Modify for production
app.run(host="127.0.0.1", port=5000, debug=False)
```

Add authentication:
```python
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    # Implement your auth logic
    return username == "admin" and password == "secure_password"

@app.route('/protected')
@auth.login_required
def protected():
    return "Protected content"
```

## 🧪 Testing

### Test RSA with sample data:

```bash
# Generate test key
openssl genrsa -out test_private.pem 1024
openssl rsa -in test_private.pem -pubout -out test_public.pem
```

Then upload `test_public.pem` through the web UI.

### Test Hash Cracking:

```bash
# Create test wordlist
echo -e "password\n123456\nadmin" > wordlist.txt

# Test hash (password = "password")
# SHA256: 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
```

## 📊 Performance Tips

1. **Wordlist size:** Larger wordlists take longer to process
2. **Rainbow tables:** Pre-compute for frequently used wordlists
3. **File uploads:** Keep files under 100 MB for best performance
4. **Birthday attack:** May run indefinitely for strong algorithms

## 🐛 Troubleshooting

### Common Issues:

**"Module not found" error:**
```bash
pip install -r reqirements.txt
```

**"Port already in use":**
```bash
# Change port in app.py
app.run(host="0.0.0.0", port=5001, debug=True)
```

**FactorDB not responding:**
- Check internet connection
- FactorDB may be slow for large numbers
- Try again later or use manual p, q input

**AES CPA fails:**
- Ensure target server is running
- Check pwntools installation
- Verify server string format

**File upload fails:**
- Check file size (max 200 MB)
- Verify file permissions
- Check `uploads/` directory exists

## 🔧 Development

### Adding New Features:

1. **Add module function** in `modules/`
2. **Create API endpoint** in `app.py`
3. **Update HTML template** in `templates/`
4. **Test functionality**

### Example - Add new hash algorithm:

```python
# modules/hashAttacker.py
def new_attack(args):
    # Your implementation
    pass

# app.py
@app.route("/api/hash/new-attack", methods=["POST"])
def api_new_attack():
    # Handle request
    pass

# templates/hash.html
// Add form and JavaScript
```

## 📝 CLI vs Web UI

Both interfaces are available:

**CLI (main.py):**
```bash
python main.py rsa_pem --public public.pem
python main.py crack --hash <hash> --algo sha256 --wordlist wordlist.txt
```

**Web UI (app.py):**
```bash
python app.py
# Open http://localhost:5000
```

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [PyCryptodome Docs](https://pycryptodome.readthedocs.io/)
- [FactorDB](http://factordb.com/)
- [Pwntools](https://docs.pwntools.com/)

## 📄 License

Use responsibly and only on systems you have permission to test.

## 🤝 Contributing

Feel free to add more features, improve UI/UX, or fix bugs!

## 📧 Support

For issues or questions, please refer to the main README.md or create an issue.

---

**Happy Hacking! 🔐**
