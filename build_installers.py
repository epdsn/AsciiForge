"""
Build script for creating AsciiForge installers for Windows, Mac, and Linux
"""
import os
import sys
import platform
import subprocess

def build_executable():
    """Build the executable using PyInstaller"""
    
    # PyInstaller options
    options = [
        'main.py',
        '--name=AsciiForge',
        '--windowed',  # No console window
        '--onefile',   # Single executable
        '--icon=icon.ico' if platform.system() == 'Windows' else '--icon=icon.icns',
        '--add-data=canvas.py;.' if platform.system() == 'Windows' else '--add-data=canvas.py:.',
        '--add-data=example.py;.' if platform.system() == 'Windows' else '--add-data=example.py:.',
        '--hidden-import=PIL',
        '--hidden-import=PIL.Image',
        '--hidden-import=PIL.ImageDraw',
        '--clean',
    ]
    
    # Remove icon option if icon file doesn't exist
    if platform.system() == 'Windows' and not os.path.exists('icon.ico'):
        options = [opt for opt in options if not opt.startswith('--icon')]
    elif platform.system() == 'Darwin' and not os.path.exists('icon.icns'):
        options = [opt for opt in options if not opt.startswith('--icon')]
    
    print(f"Building AsciiForge for {platform.system()}...")
    print(f"PyInstaller command: pyinstaller {' '.join(options)}")
    
    try:
        subprocess.run(['pyinstaller'] + options, check=True)
        print("\n✓ Build completed successfully!")
        print(f"Executable location: dist/AsciiForge")
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Build failed: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("\n✗ PyInstaller not found. Install it with: pip install pyinstaller")
        sys.exit(1)

def main():
    """Main build function"""
    print("=" * 60)
    print("AsciiForge Installer Builder")
    print("=" * 60)
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print("=" * 60)
    
    build_executable()
    
    print("\n" + "=" * 60)
    print("Build Process Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
