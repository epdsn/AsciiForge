# AsciiForge Installation Guide

This guide provides instructions for building and installing AsciiForge on Windows, macOS, and Linux.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- All dependencies from `requirements.txt`

## Building from Source

### Windows

1. **Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   pip install pyinstaller
   ```

2. **Build the installer:**
   ```cmd
   build_windows.bat
   ```

3. **Run the application:**
   - The executable will be created in `dist\AsciiForge.exe`
   - Double-click to run, or run from command line:
     ```cmd
     dist\AsciiForge.exe
     ```

### macOS

1. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   pip3 install pyinstaller
   ```

2. **Make the build script executable:**
   ```bash
   chmod +x build_unix.sh
   ```

3. **Build the application:**
   ```bash
   ./build_unix.sh
   ```

4. **Run the application:**
   - The app bundle will be created at `dist/AsciiForge.app`
   - Double-click to run, or run from terminal:
     ```bash
     open dist/AsciiForge.app
     ```

### Linux

1. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   pip3 install pyinstaller
   ```

2. **Make the build script executable:**
   ```bash
   chmod +x build_unix.sh
   ```

3. **Build the executable:**
   ```bash
   ./build_unix.sh
   ```

4. **Run the application:**
   ```bash
   ./dist/AsciiForge
   ```

## Manual Build (All Platforms)

If you prefer to build manually:

```bash
# Install PyInstaller
pip install pyinstaller

# Build using the spec file
pyinstaller AsciiForge.spec

# Or use the build script
python build_installers.py
```

## Distribution

### Windows
- Distribute the `AsciiForge.exe` file from the `dist` folder
- Users can run it directly without Python installed

### macOS
- Distribute the `AsciiForge.app` bundle from the `dist` folder
- Users can drag it to their Applications folder
- Note: First-time users may need to right-click and select "Open" to bypass Gatekeeper

### Linux
- Distribute the `AsciiForge` executable from the `dist` folder
- Make sure it has execute permissions: `chmod +x AsciiForge`
- Users may need to install tkinter: `sudo apt-get install python3-tk` (on Debian/Ubuntu)

## Troubleshooting

### Missing Dependencies
If the built application fails to run due to missing modules:
```bash
pyinstaller --onefile --windowed --hidden-import=MODULE_NAME main.py
```

### Icon Not Found
If you get icon-related errors during build:
- Remove the `--icon` flag from `build_installers.py`
- Or create appropriate icon files (`icon.ico` for Windows, `icon.icns` for macOS)

### tkinter Issues on Linux
If you get tkinter errors:
```bash
sudo apt-get install python3-tk
```

### Pillow/PIL Issues
Ensure Pillow is properly installed:
```bash
pip install --upgrade Pillow
```

## Creating Installers

### Windows Installer (Advanced)
To create a Windows installer (.msi or .exe), you can use:
- **Inno Setup**: Free installer creator for Windows
- **NSIS**: Nullsoft Scriptable Install System

### macOS DMG (Advanced)
To create a DMG installer:
```bash
# Install create-dmg
brew install create-dmg

# Create DMG
create-dmg \
  --volname "AsciiForge" \
  --window-pos 200 120 \
  --window-size 800 400 \
  --icon-size 100 \
  --app-drop-link 600 185 \
  "AsciiForge-Installer.dmg" \
  "dist/AsciiForge.app"
```

### Linux Package (Advanced)
For Linux distributions, consider creating:
- **.deb package** (Debian/Ubuntu): Use `dpkg-deb` or `checkinstall`
- **.rpm package** (Fedora/RedHat): Use `rpmbuild`
- **AppImage**: Use `appimagetool` for universal Linux compatibility
- **Flatpak** or **Snap**: For modern Linux app stores

## Version Information

Current version: 1.0.0

For more information, visit the project repository.
