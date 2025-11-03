# Changelog

All notable changes to the Cryptanalyzer project.

## [2.0.0] - Web UI Release

### 🎉 Major Features Added

#### Web Interface
- ✨ **Complete Flask-based Web UI**
  - Modern, responsive design with Tailwind CSS
  - Dark theme optimized for security tools
  - Interactive dashboard with 4 main modules
  - Real-time output display

#### New Modules & Functions
- ✨ **Enhanced RSA Module** (`modules/rsa.py`)
  - Added `rsa_fact()` - Factor n and decrypt
  - Added `rsa()` - Direct decryption with p, q
  - Added `rsa_e()` - Small exponent attack (e=3)
  - Improved error handling and output

#### Launch Scripts
- ✨ **run_webui.sh** - Automated launcher for Linux/Mac
  - Creates virtual environment automatically
  - Installs dependencies
  - Starts Flask server
- ✨ **run_webui.bat** - Windows launcher
  - Same features for Windows users

#### Configuration System
- ✨ **config.py** - Centralized configuration
  - Development, Production, Testing configs
  - Easy customization of host, port, security settings
  - Environment-based configuration loading

#### Frontend Assets
- ✨ **static/css/style.css** - Custom styling
  - Professional dark theme
  - Smooth animations and transitions
  - Responsive design
  - Custom scrollbars and hover effects
- ✨ **static/js/utils.js** - JavaScript utilities
  - API call helpers
  - Output formatting functions
  - File upload utilities
  - Notification system

#### Documentation
- ✨ **WEB_UI_README.md** - Comprehensive web UI guide
  - Complete API documentation
  - Security considerations
  - Deployment instructions
  - Troubleshooting guide
- ✨ **QUICKSTART.md** - Quick start guide
  - 3-step setup process
  - Common use cases
  - Example attacks
  - Tips and tricks
- ✨ **WEB_UI_SETUP_COMPLETE.md** - Setup summary
  - Complete file listing
  - Verification checklist
  - Usage examples
- ✨ **Updated README.md** - Enhanced main documentation
  - Professional formatting
  - Comprehensive feature list
  - Usage examples
  - Security guidelines

#### Testing
- ✨ **test_webui.py** - Automated test suite
  - Tests all major endpoints
  - Validates functionality
  - Easy verification of installation

#### Sample Data
- ✨ **data/sample_wordlist.txt** - Sample wordlist for testing
  - Common passwords for hash cracking demos

### 🔧 Improvements

#### Backend
- 🔄 **Updated app.py**
  - Now uses config system
  - Better error handling
  - Improved output capture
  - Enhanced API responses

#### Dependencies
- 📦 **Updated reqirements.txt**
  - Added `gmpy2==2.1.5` for RSA math operations
  - Added `Werkzeug==2.3.6` for Flask utilities
  - Version pinning for stability

#### Templates
- 🎨 **Enhanced all HTML templates**
  - Linked to custom CSS
  - Added JavaScript utilities
  - Improved user experience
  - Better error display

### 📋 File Structure

#### New Files Created
```
static/
├── css/
│   └── style.css           # Custom styling (NEW)
└── js/
    └── utils.js            # JavaScript utilities (NEW)

data/
└── sample_wordlist.txt     # Sample wordlist (NEW)

Documentation:
├── WEB_UI_README.md        # Web UI docs (NEW)
├── QUICKSTART.md           # Quick start (NEW)
├── WEB_UI_SETUP_COMPLETE.md # Setup summary (NEW)
└── CHANGELOG.md            # This file (NEW)

Scripts:
├── run_webui.sh            # Linux/Mac launcher (NEW)
├── run_webui.bat           # Windows launcher (NEW)
├── test_webui.py           # Test suite (NEW)
└── config.py               # Configuration (NEW)
```

#### Modified Files
```
├── app.py                  # Added config support (MODIFIED)
├── modules/rsa.py          # Added new functions (MODIFIED)
├── reqirements.txt         # Added dependencies (MODIFIED)
├── README.md               # Complete rewrite (MODIFIED)
└── templates/*.html        # Linked new assets (MODIFIED)
```

### 🛠️ Technical Details

#### Architecture
- **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript
- **Backend:** Flask 2.3.2, Python 3.7+
- **APIs:** RESTful JSON endpoints
- **Storage:** File-based uploads, no database required

#### Security
- File upload validation
- Secure filename handling
- Configurable upload limits (200 MB default)
- Environment-based security settings
- CSRF protection ready

#### Performance
- Async API calls on frontend
- Streaming output capture
- Efficient file handling
- Optimized for local deployment

### 📊 Statistics

- **New Files:** 12
- **Modified Files:** 6
- **Lines of Code Added:** ~2,500+
- **Documentation Pages:** 4
- **API Endpoints:** 12
- **Test Cases:** 6

### 🐛 Bug Fixes

- Fixed missing RSA functions referenced in main.py
- Added proper error handling in all API endpoints
- Resolved import issues in app.py
- Fixed file upload path handling

### 🔐 Security Notes

- All user inputs properly sanitized
- File uploads use secure_filename()
- Default configuration for local use only
- Production config available for deployment
- Session security configured

### 📚 Documentation Improvements

- Added comprehensive API documentation
- Created step-by-step tutorials
- Included usage examples
- Added troubleshooting guides
- Security best practices documented

### 🎯 Future Enhancements (Roadmap)

Potential future additions:
- [ ] Authentication system (OAuth, JWT)
- [ ] Rate limiting for API endpoints
- [ ] WebSocket support for real-time updates
- [ ] Database integration for results history
- [ ] Advanced RSA attacks (Wiener, Coppersmith)
- [ ] More hash algorithms support
- [ ] Batch processing capabilities
- [ ] Export results to various formats
- [ ] API key management
- [ ] User profiles and saved sessions

### 🙏 Acknowledgments

- Flask community for excellent framework
- Tailwind CSS for beautiful styling
- PyCryptodome for crypto operations
- All security researchers and contributors

---

## [1.0.0] - Initial CLI Release

### Features
- ✅ RSA PEM extraction
- ✅ Hash cracking (dictionary attacks)
- ✅ AES chosen plaintext attacks
- ✅ Encoding/decoding utilities
- ✅ Command-line interface
- ✅ Basic documentation

---

**Note:** Version 2.0.0 represents a major upgrade with the addition of the complete Web UI while maintaining full backward compatibility with the CLI interface.
