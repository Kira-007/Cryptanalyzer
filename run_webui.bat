@echo off
REM Cryptanalyzer Web UI Launcher for Windows

echo ==========================================
echo   🔐 Cryptanalyzer Web UI
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3 first.
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv\" (
    echo 📦 Virtual environment not found. Creating one...
    python -m venv venv
    echo ✅ Virtual environment created.
)

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/update dependencies
echo 📥 Installing dependencies...
pip install -q --upgrade pip
pip install -q -r reqirements.txt

if errorlevel 1 (
    echo ❌ Failed to install dependencies. Please check reqirements.txt
    pause
    exit /b 1
)

echo ✅ Dependencies installed.
echo.

REM Create uploads directory if it doesn't exist
if not exist "uploads\" mkdir uploads

REM Start the Flask server
echo 🚀 Starting Flask web server...
echo 📍 Server will be available at: http://localhost:5000
echo ⚠️  Press Ctrl+C to stop the server
echo.
echo ==========================================
echo.

python app.py
pause
