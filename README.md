# AsciiForge

**AsciiForge** is an interactive Python application that lets you create, view, and manage ASCII art. Whether you want to convert images to ASCII art, browse a collection of predefined ASCII art pieces, or create your own masterpieces from scratch, AsciiForge provides an intuitive menu-driven interface to bring your text-based artwork to life.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the main interactive application:

```bash
python main.py
```

The program will present you with the following options:
1. **Convert an image to ASCII art** - Transform your images into text-based art
2. **View predefined ASCII art pieces** - Browse and display built-in ASCII art from the collection
3. **Create your own ASCII art** - Design custom ASCII art from scratch
4. **Exit** - Close the application

### Additional Tools

#### Show sample ASCII art
```bash
python ascii_art_tester.py -s
```

#### Convert image to ASCII art
```bash
python ascii_art_tester.py -f image.jpg
python ascii_art_tester.py -f image.png -w 150  # custom width
```

#### Display ASCII art text
```bash
python ascii_art_tester.py -t "Your ASCII art here"
```

## Features

- Convert images to ASCII art
- Display and test ASCII art strings
- Adjustable output width
- Save ASCII art to file
- Built-in sample art for quick testing
