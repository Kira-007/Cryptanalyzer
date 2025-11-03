#!/bin/bash

# Cryptanalyzer Web UI Launcher
# This script starts the Flask web server

echo "=========================================="
echo "  🔐 Cryptanalyzer Web UI"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Virtual environment not found. Creating one..."
    python3 -m venv venv
    echo "✅ Virtual environment created."
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📥 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r reqirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies. Please check reqirements.txt"
    exit 1
fi

echo "✅ Dependencies installed."
echo ""

# Create uploads directory if it doesn't exist
mkdir -p uploads

# Start the Flask server
echo "🚀 Starting Flask web server..."
echo "📍 Server will be available at: http://localhost:5000"
echo "⚠️  Press Ctrl+C to stop the server"
echo ""
echo "=========================================="
echo ""

python3 app.py
