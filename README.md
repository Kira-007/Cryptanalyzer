# 🔐 Cryptanalyzer

<p align="center">
  <b>A powerful Cryptographic analysis toolkit with Web UI and CLI interfaces</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Flask-2.3+-green.svg" alt="Flask">
  <img src="https://img.shields.io/badge/License-Educational-red.svg" alt="License">
</p>

---

## 📋 Overview

**Cryptanalyzer** is a comprehensive toolkit for analyzing and attacking widely-used cryptographic algorithms including RSA, AES, and various hash functions. It provides both a modern web interface and a powerful command-line interface for security researchers, CTF players, and penetration testers.

### ✨ Key Features

- 🌐 **Modern Web UI** - User-friendly Flask-based interface
- 💻 **Powerful CLI** - Command-line interface for automation
- 🔑 **RSA Attacks** - Factorization, PEM extraction, small exponent attacks
- 🔒 **AES Analysis** - Chosen plaintext attacks, oracle exploitation
- #️⃣ **Hash Cracking** - Dictionary attacks, rainbow tables, HMAC brute-force
- 🎯 **Birthday Attacks** - Collision finding demonstrations
- 🔤 **Encoding Tools** - Base64, Hex, URL encode/decode

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Cryptanalyzer.git
cd Cryptanalyzer

# Install dependencies
pip install -r reqirements.txt
```

### Launch Web UI (Recommended)

**Linux/Mac:**
```bash
./run_webui.sh
```

**Windows:**
```cmd
run_webui.bat
```

**Manual:**
```bash
python app.py
```

Then open: **http://localhost:5000**

### CLI Usage

```bash
# RSA attacks
python main.py rsa_pem --public public.pem
python main.py rsa -n 143 -e 7 -c 2

# Hash cracking
python main.py crack --hash 5f4dcc3b5aa765d61d8327deb882cf99 --algo md5 --wordlist wordlist.txt

# Encoding/Decoding
python main.py base64-encode --data "Hello World"
python main.py hex-decode --data "48656c6c6f"

# AES attacks
python main.py aes --server 127.0.0.1:1337
```

---

## 📚 Documentation

- **🚀 [Quick Start Guide](QUICKSTART.md)** - Get started in 3 steps
- **📖 [Web UI Documentation](WEB_UI_README.md)** - Complete web interface guide
- **✅ [Setup Complete Guide](WEB_UI_SETUP_COMPLETE.md)** - Everything that was set up
- **💻 CLI Help** - Run `python main.py --help`

---

## 🛠️ Features in Detail

### 🔑 RSA Tools

- **PEM Key Extraction** - Extract n, e from public key files
- **Automatic Factorization** - Uses FactorDB to factor weak RSA moduli
- **Private Key Recovery** - Generates private keys from factored moduli
- **Small Exponent Attack** - Exploits e=3 vulnerabilities
- **Direct Decryption** - Given p, q, decrypt ciphertext

### 🔒 AES Analysis

- **Chosen Plaintext Attack (CPA)** - Exploits encryption oracles
- **Padding Oracle Attacks** - Exploits CBC padding vulnerabilities
- **Interactive Oracle** - Uses pwntools for server interaction

### #️⃣ Hash Attacks

- **Dictionary Attacks** - Brute-force with wordlists
- **Rainbow Tables** - Pre-computed hash tables
  - Generate tables from wordlists
  - Instant lookups
- **HMAC Brute-force** - Crack HMAC secret keys
- **Birthday Attacks** - Demonstrate collision finding
- **Supported Algorithms** - MD5, SHA1, SHA256, SHA512, and more

### 🔤 Encoding/Decoding

- **Base64** - Encode/Decode
- **Hexadecimal** - Encode/Decode
- **URL Encoding** - Encode/Decode

---

## 📁 Project Structure

```
Cryptanalyzer/
├── app.py                  # Flask web application
├── main.py                 # CLI interface
├── config.py               # Configuration
├── run_webui.sh            # Linux/Mac launcher
├── run_webui.bat           # Windows launcher
├── test_webui.py           # Test suite
├── reqirements.txt         # Dependencies
│
├── modules/                # Core analysis modules
│   ├── rsa.py             # RSA attacks
│   ├── aes.py             # AES attacks
│   └── hashAttacker.py    # Hash attacks & encoding
│
├── templates/              # Web UI templates
│   ├── index.html         # Dashboard
│   ├── rsa.html           # RSA tools
│   ├── aes.html           # AES tools
│   ├── hash.html          # Hash attacks
│   └── encode.html        # Encoding tools
│
├── static/                 # Frontend assets
│   ├── css/style.css      # Custom styling
│   └── js/utils.js        # JavaScript utilities
│
└── data/                   # Data files
    └── sample_wordlist.txt # Sample wordlist
```

---

## 🧪 Testing

Run the automated test suite:

```bash
# Start the server
python app.py &

# Run tests
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

---

## 💡 Usage Examples

### Example 1: Crack a Password Hash

**Web UI:**
1. Navigate to http://localhost:5000/hash
2. Enter hash: `5f4dcc3b5aa765d61d8327deb882cf99`
3. Select algorithm: `md5`
4. Upload wordlist: `data/sample_wordlist.txt`
5. Click "Run Crack"
6. Result: `password`

**CLI:**
```bash
python main.py crack \
  --hash 5f4dcc3b5aa765d61d8327deb882cf99 \
  --algo md5 \
  --wordlist data/sample_wordlist.txt
```

### Example 2: Factor Weak RSA Key

**Web UI:**
1. Navigate to http://localhost:5000/rsa
2. Enter: n=143, e=7, c=2
3. Click "Run"
4. View decrypted plaintext

**CLI:**
```bash
python main.py rsa -n 143 -e 7 -c 2
```

### Example 3: Generate Rainbow Table

**Web UI:**
1. Navigate to http://localhost:5000/hash
2. Select algorithm: `sha256`
3. Upload wordlist
4. Enter output filename: `rainbow_sha256.json`
5. Click "Generate"
6. Download generated table

**CLI:**
```bash
python main.py rainbow-gen \
  --algo sha256 \
  --wordlist data/sample_wordlist.txt \
  --output rainbow_sha256.json
```

---

## 🔒 Security & Ethics

### ⚠️ DISCLAIMER

**This tool is for EDUCATIONAL and AUTHORIZED SECURITY TESTING purposes ONLY.**

- ✅ Use on systems you own or have explicit permission to test
- ✅ Use for CTF competitions and security research
- ✅ Use for learning cryptography concepts
- ❌ Do NOT use for illegal activities
- ❌ Do NOT use without authorization
- ❌ Do NOT expose web UI to the internet without authentication

### Security Best Practices

- **Local Use Only** - Default configuration binds to all interfaces
- **Add Authentication** - See `WEB_UI_README.md` for examples
- **Use Strong Passwords** - If deploying with authentication
- **Keep Updated** - Regularly update dependencies
- **Secure Configuration** - Use `ProductionConfig` for production

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Adding New Features

1. **Add module function** in `modules/`
2. **Create API endpoint** in `app.py`
3. **Update HTML template** in `templates/`
4. **Add tests** in `test_webui.py`
5. **Update documentation**

---

## 📦 Dependencies

- **Flask** - Web framework
- **PyCryptodome** - Cryptographic operations
- **pwntools** - Binary exploitation toolkit
- **factordb-pycli** - RSA factorization
- **gmpy2** - Number theory operations
- **requests** - HTTP library

See `reqirements.txt` for complete list.

---

## 🎓 Learning Resources

- [CryptoHack](https://cryptohack.org/) - Interactive cryptography challenges
- [Cryptopals](https://cryptopals.com/) - Crypto challenges
- [FactorDB](http://factordb.com/) - Integer factorization database
- [HashCat Wiki](https://hashcat.net/wiki/) - Password recovery
- [RSA CTF Tool](https://github.com/RsaCtfTool/RsaCtfTool) - Advanced RSA attacks

---

## 📝 License

This project is for educational purposes. Use responsibly and ethically.

---

## 🙏 Acknowledgments

- Thanks to all contributors and security researchers
- Inspired by various CTF challenges and security tools
- Built with modern web technologies and cryptographic libraries

---

## 📧 Support

For issues, questions, or suggestions:

- 📖 Check the documentation files
- 🐛 Open an issue on GitHub
- 💬 Review existing issues and discussions

---

<p align="center">
  <b>⚡ Happy Hacking! ⚡</b><br>
  <i>Remember: With great power comes great responsibility.</i>
</p>

---

**Made with ❤️ for the security community**
