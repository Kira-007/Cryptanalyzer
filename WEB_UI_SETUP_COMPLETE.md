# 🎉 Cryptanalyzer Web UI - Setup Complete!

Your web UI is now fully configured and ready to use!

## 📦 What Was Created

### 🚀 Launch Scripts
- ✅ `run_webui.sh` - Linux/Mac launcher
- ✅ `run_webui.bat` - Windows launcher

### ⚙️ Configuration
- ✅ `config.py` - Centralized configuration file
- ✅ Updated `app.py` - Now uses config system
- ✅ Updated `reqirements.txt` - Added gmpy2 and Werkzeug

### 🎨 Frontend Assets
- ✅ `static/css/style.css` - Custom styling
- ✅ `static/js/utils.js` - JavaScript utilities
- ✅ Updated all HTML templates to use new assets

### 🔧 Enhanced Modules
- ✅ `modules/rsa.py` - Added missing functions:
  - `rsa_fact()` - Factor and decrypt
  - `rsa()` - Direct decryption with p, q
  - `rsa_e()` - Small exponent attack

### 📚 Documentation
- ✅ `WEB_UI_README.md` - Complete web UI documentation
- ✅ `QUICKSTART.md` - Quick start guide
- ✅ `WEB_UI_SETUP_COMPLETE.md` - This file!

### 🧪 Testing
- ✅ `test_webui.py` - Automated test suite
- ✅ `data/sample_wordlist.txt` - Sample wordlist for testing

## 🚀 Quick Start (3 Steps!)

### Step 1: Install Dependencies
```bash
pip install -r reqirements.txt
```

### Step 2: Start Server

**On Linux/Mac:**
```bash
./run_webui.sh
```

**On Windows:**
```cmd
run_webui.bat
```

**Or manually:**
```bash
python app.py
```

### Step 3: Open Browser
Navigate to: **http://localhost:5000**

## 🧪 Verify Installation

Run the test suite:
```bash
# First, start the server in one terminal
python app.py

# Then in another terminal, run tests
python test_webui.py
```

Expected output:
```
✅ PASS - Homepage
✅ PASS - Pages
✅ PASS - Encoding
✅ PASS - Hash Crack
✅ PASS - RSA Factor
✅ PASS - Birthday Attack

🎉 All tests passed!
```

## 🎯 Features Available

### 1️⃣ RSA Tools (`/rsa`)
- Extract keys from PEM files
- Factor RSA modulus
- Decrypt ciphertext
- Small exponent attacks

### 2️⃣ Hash Attacks (`/hash`)
- Dictionary/brute-force cracking
- Rainbow table generation
- Rainbow table lookup
- HMAC brute-force
- Birthday attack demonstration

### 3️⃣ AES Tools (`/aes`)
- Chosen plaintext attacks
- Oracle exploitation

### 4️⃣ Encoding/Decoding (`/encode`)
- Base64 encode/decode
- Hex encode/decode
- URL encode/decode

## 📁 Project Structure

```
Cryptanalyzer/
├── 🚀 Launch Scripts
│   ├── run_webui.sh       # Linux/Mac launcher
│   └── run_webui.bat      # Windows launcher
│
├── ⚙️ Core Application
│   ├── app.py             # Flask web server
│   ├── config.py          # Configuration
│   ├── main.py            # CLI interface
│   └── reqirements.txt    # Dependencies
│
├── 🧩 Modules
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── rsa.py         # RSA attacks (ENHANCED)
│   │   ├── aes.py         # AES attacks
│   │   └── hashAttacker.py # Hash attacks
│
├── 🎨 Frontend
│   ├── templates/
│   │   ├── index.html     # Dashboard
│   │   ├── rsa.html       # RSA tools
│   │   ├── aes.html       # AES tools
│   │   ├── hash.html      # Hash attacks
│   │   └── encode.html    # Encoding tools
│   │
│   └── static/
│       ├── css/
│       │   └── style.css  # Custom styles
│       └── js/
│           └── utils.js   # JavaScript utilities
│
├── 📚 Documentation
│   ├── WEB_UI_README.md   # Full web UI docs
│   ├── QUICKSTART.md      # Quick start guide
│   ├── README.md          # Main project README
│   └── WEB_UI_SETUP_COMPLETE.md  # This file
│
├── 🧪 Testing
│   └── test_webui.py      # Test suite
│
└── 📊 Data
    ├── data/
    │   └── sample_wordlist.txt  # Sample wordlist
    └── uploads/           # User uploads (auto-created)
```

## 🔐 Security Reminders

⚠️ **IMPORTANT:**
- This tool is for **authorized security testing only**
- **DO NOT** expose to the internet without authentication
- Default binding: `0.0.0.0:5000` (all interfaces)
- For production: Set `HOST=127.0.0.1` in `config.py`

## 🎨 Customization

### Change Port
Edit `config.py`:
```python
PORT = 5001  # Change to your preferred port
```

### Change Theme
Edit `static/css/style.css`:
```css
:root {
  --accent-cyan: #06b6d4;  /* Change primary color */
}
```

### Add Authentication
See `WEB_UI_README.md` for authentication examples.

## 📖 Documentation Quick Links

- **Getting Started:** `QUICKSTART.md`
- **Full Documentation:** `WEB_UI_README.md`
- **CLI Usage:** Run `python main.py --help`
- **API Reference:** See `WEB_UI_README.md` → API Endpoints

## 🐛 Troubleshooting

### Server won't start
```bash
# Check if port is in use
lsof -i :5000  # Linux/Mac
netstat -ano | findstr :5000  # Windows

# Use different port
python app.py  # Will use port from config.py
```

### Module not found
```bash
pip install -r reqirements.txt
```

### Tests failing
```bash
# Ensure server is running first
python app.py &
sleep 2
python test_webui.py
```

## 💡 Usage Examples

### Example 1: Crack MD5 Hash
1. Go to http://localhost:5000/hash
2. Hash: `5f4dcc3b5aa765d61d8327deb882cf99`
3. Algo: `md5`
4. Upload: `data/sample_wordlist.txt`
5. Click "Run Crack"
6. Result: `password`

### Example 2: RSA Factorization
1. Go to http://localhost:5000/rsa
2. n: `143` (= 11 × 13)
3. e: `7`
4. c: `2`
5. Click "Run"
6. See decrypted plaintext!

### Example 3: Base64 Encoding
1. Go to http://localhost:5000/encode
2. Select "Base64 Encode"
3. Enter text: `Hello, World!`
4. Click "Run"
5. Result: `SGVsbG8sIFdvcmxkIQ==`

## 🤝 Contributing

Want to add features? Here's how:

1. **Add module function** in `modules/`
2. **Create API endpoint** in `app.py`
3. **Update HTML template** in `templates/`
4. **Add tests** in `test_webui.py`
5. **Update docs** in `WEB_UI_README.md`

## 🎓 Learning Resources

- Flask Tutorial: https://flask.palletsprojects.com/
- Cryptography Basics: https://cryptohack.org/
- RSA Attacks: https://github.com/RsaCtfTool/RsaCtfTool
- Hash Cracking: https://hashcat.net/wiki/

## 📧 Need Help?

- Read the documentation files
- Check the test suite for examples
- Review the code comments
- Test with sample data

## ✅ Verification Checklist

Before you start using the web UI, verify:

- [ ] Dependencies installed: `pip install -r reqirements.txt`
- [ ] Server starts: `python app.py`
- [ ] Homepage loads: http://localhost:5000
- [ ] Tests pass: `python test_webui.py`
- [ ] Sample attack works (see examples above)

## 🎉 You're All Set!

Your Cryptanalyzer Web UI is fully configured and ready to use!

Start the server:
```bash
./run_webui.sh  # or python app.py
```

Open browser:
```
http://localhost:5000
```

**Happy Hacking! 🔐**

---

*For detailed information, see:*
- *Quick Start: `QUICKSTART.md`*
- *Full Docs: `WEB_UI_README.md`*
- *CLI Usage: `python main.py --help`*
