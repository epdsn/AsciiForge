# AsciiForge

**AsciiForge** is an interactive Python application that lets you create, view, and manage ASCII art. Whether you want to convert images to ASCII art, browse a collection of predefined ASCII art pieces, or draw your own creations using a graphical canvas, AsciiForge provides both an intuitive menu-driven interface and a visual drawing tool to bring your text-based artwork to life.

## Installation

### Setting up Python Environment in VS Code

1. **Create a Python virtual environment:**
   - Press `Ctrl+Shift+P` in VS Code
   - Type "Python: Create Environment" and select it
   - Choose **Venv** as the environment type
   - Select your Python interpreter
   - Check the box to install dependencies from `requirements.txt`

2. **Or install manually:**
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
3. **Create your own ASCII art** - Draw on a graphical canvas and convert to ASCII art
4. **Exit** - Close the application

### Creating ASCII Art with the Drawing Canvas

When you select option 3, a graphical window will open with:
- **Black canvas** for drawing
- **White pen** for creating your artwork
- **Mouse controls** - Click and drag to draw
- **Pen size buttons** - Choose from 1, 3, 5, 8, or 12 pixel brush sizes
- **Clear button** - Erase and start over
- **Preview ASCII** - See your drawing converted to ASCII in real-time
- **Convert & Save** - Export your creation as ASCII art to a text file

### Using in Visual Studio Code

#### Running the Application

1. **Open the integrated terminal** in VS Code:
   - Press `` Ctrl+` `` (backtick) or go to `Terminal > New Terminal`

2. **Run the main application**:
   ```bash
   python main.py
   ```

3. **Alternative: Run directly from the editor**:
   - Open [main.py](main.py) in the editor
   - Press `F5` or click `Run > Start Debugging`
   - Or right-click in the editor and select `Run Python File in Terminal`

#### Using the ASCII Art Tester

You can run the tester tools directly from the VS Code terminal:

```bash
# List all available ASCII art
python ascii_art_tester.py -l

# Display specific art from canvas
python ascii_art_tester.py -c cat

# Convert an image
python ascii_art_tester.py -f path/to/image.jpg
```

#### Tips for VS Code

- Use the **Output pane** to view results when running with F5
- The **integrated terminal** is best for interactive prompts
- Install the **Python extension** for enhanced debugging and IntelliSense
- Use **Ctrl+Shift+P** and type "Python: Select Interpreter" to ensure the correct Python environment

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

- **Image to ASCII Conversion** - Transform any image into ASCII art
- **Predefined ASCII Art Library** - Browse and display built-in ASCII art pieces
- **Graphical Drawing Canvas** - Draw freehand with your mouse and convert to ASCII
- **Interactive Canvas Tools** - Multiple pen sizes and real-time preview
- **Export Functionality** - Save your ASCII creations to text files
- **Menu-Driven Interface** - Easy-to-use command-line menu system

## Future Roadmap

AsciiForge is actively being developed with exciting new features planned:

### FastAPI Web Service
- RESTful API endpoints for image-to-ASCII conversion
- Web-based interface for creating and viewing ASCII art
- API documentation and interactive testing with Swagger UI
- Cloud deployment for easy access from anywhere

### Web Application
- Modern responsive web interface
- Real-time ASCII art preview and editing
- Share and export ASCII art creations
- Cloud storage for saved artworks
- Cross-platform accessibility from any browser

### Mobile Application
- Native iOS and Android apps
- Touch-optimized ASCII art editor
- Camera integration for instant image-to-ASCII conversion
- Offline mode for creating art on the go
- Social sharing features

