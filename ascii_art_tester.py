#!/usr/bin/env python3
"""
ASCII Art Tester - A simple tool for testing and displaying ASCII art
"""

import sys
from PIL import Image
import argparse
import canvas


ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']


def resize_image(image, new_width=100):
    """Resize image maintaining aspect ratio"""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  # 0.55 to adjust for character height
    return image.resize((new_width, new_height))


def grayscale(image):
    """Convert image to grayscale"""
    return image.convert('L')


def pixels_to_ascii(image):
    """Convert pixels to ASCII characters"""
    pixels = image.getdata()
    ascii_str = ''
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str


def image_to_ascii(image_path, width=100):
    """Convert image to ASCII art"""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return None
    
    image = resize_image(image, width)
    image = grayscale(image)
    
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    
    ascii_art = '\n'.join([ascii_str[i:i+img_width] for i in range(0, len(ascii_str), img_width)])
    return ascii_art


def display_ascii_art(art):
    """Display ASCII art"""
    print("\n" + "="*80)
    print(art)
    print("="*80 + "\n")


def test_ascii_string(text):
    """Test displaying a simple ASCII art string"""
    display_ascii_art(text)


def main():
    parser = argparse.ArgumentParser(description='Test ASCII art')
    parser.add_argument('-f', '--file', help='Image file to convert to ASCII')
    parser.add_argument('-w', '--width', type=int, default=100, help='Width of ASCII output (default: 100)')
    parser.add_argument('-t', '--text', help='ASCII art text to display')
    parser.add_argument('-s', '--sample', action='store_true', help='Show sample ASCII art')
    parser.add_argument('-c', '--canvas', help='Display ASCII art from canvas by name')
    parser.add_argument('-l', '--list', action='store_true', help='List all available canvas art')
    parser.add_argument('-a', '--all', action='store_true', help='Display all canvas art')
    
    args = parser.parse_args()
    
    if args.list:
        print("\nAvailable ASCII art in canvas:")
        for name in canvas.list_art():
            print(f"  - {name}")
        print(f"\nTotal: {len(canvas.list_art())} pieces")
        print("\nUse: python ascii_art_tester.py -c <name>")
    
    elif args.all:
        all_art = canvas.get_all_art()
        for name, art in all_art.items():
            print(f"\n{'='*80}")
            print(f"  {name.upper()}")
            print('='*80)
            print(art)
    
    elif args.canvas:
        art = canvas.get_art(args.canvas)
        if art:
            print(f"\nASCII Art - '{args.canvas}':")
            display_ascii_art(art)
        else:
            print(f"Error: '{args.canvas}' not found in canvas.")
            print("Available art:", ", ".join(canvas.list_art()))
    
    elif args.sample:
        sample_art = """
    /\\_/\\  
   ( o.o ) 
    > ^ <
   /|   |\\
  (_|   |_)
        """
        print("\nSample ASCII Art - Cat:")
        display_ascii_art(sample_art)
    
    elif args.file:
        print(f"Converting image: {args.file}")
        ascii_art = image_to_ascii(args.file, args.width)
        if ascii_art:
            display_ascii_art(ascii_art)
            
            # Option to save
            save = input("Save to file? (y/n): ")
            if save.lower() == 'y':
                filename = input("Enter filename (default: output.txt): ") or "output.txt"
                with open(filename, 'w') as f:
                    f.write(ascii_art)
                print(f"Saved to {filename}")
    
    elif args.text:
        display_ascii_art(args.text)
    
    else:
        parser.print_help()
        print("\nExamples:")
        print("  python ascii_art_tester.py -l                    # List all canvas art")
        print("  python ascii_art_tester.py -c cat                # Display 'cat' from canvas")
        print("  python ascii_art_tester.py -a                    # Display all canvas art")
        print("  python ascii_art_tester.py -s                    # Show sample ASCII art")
        print("  python ascii_art_tester.py -f image.jpg          # Convert image to ASCII")
        print("  python ascii_art_tester.py -f image.jpg -w 150   # Convert with custom width")
        print("  python ascii_art_tester.py -t 'Hello World'      # Display text")


if __name__ == "__main__":
    main()
