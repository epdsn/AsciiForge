#!/bin/bash
# Build script for Linux and macOS

echo "========================================"
echo "AsciiForge Installer Builder"
echo "========================================"

# Check if PyInstaller is installed
if ! python3 -c "import PyInstaller" 2>/dev/null; then
    echo "PyInstaller not found. Installing..."
    pip3 install pyinstaller
fi

# Build the executable
echo "Building AsciiForge..."
python3 build_installers.py

if [ $? -ne 0 ]; then
    echo "Build failed!"
    exit 1
fi

echo ""
echo "========================================"
echo "Build Complete!"
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Application: dist/AsciiForge.app"
else
    echo "Executable: dist/AsciiForge"
fi
echo "========================================"
