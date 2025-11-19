@echo off
REM Build script for Windows

echo ========================================
echo AsciiForge Windows Installer Builder
echo ========================================

REM Check if PyInstaller is installed
python -c "import PyInstaller" 2>NUL
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
)

REM Build the executable
echo Building AsciiForge for Windows...
python build_installers.py

if errorlevel 1 (
    echo Build failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build Complete!
echo Executable: dist\AsciiForge.exe
echo ========================================
pause
