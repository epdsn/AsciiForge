"""
Canvas module for AsciiForge - Interactive ASCII art drawing
"""
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageDraw
import io

class AsciiCanvas:
    """Interactive canvas for creating ASCII art"""
    
    def __init__(self, width=80, height=24):
        """Initialize canvas with given dimensions"""
        self.width = width
        self.height = height
        self.canvas = [[' ' for _ in range(width)] for _ in range(height)]
        
    def clear(self):
        """Clear the canvas"""
        self.canvas = [[' ' for _ in range(self.width)] for _ in range(self.height)]
    
    def set_pixel(self, x, y, char='█'):
        """Set a character at position (x, y)"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.canvas[y][x] = char
    
    def draw_line(self, x1, y1, x2, y2, char='█'):
        """Draw a line from (x1, y1) to (x2, y2)"""
        # Bresenham's line algorithm
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        
        while True:
            self.set_pixel(x1, y1, char)
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy
    
    def draw_rectangle(self, x1, y1, x2, y2, char='█', fill=False):
        """Draw a rectangle"""
        if fill:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    self.set_pixel(x, y, char)
        else:
            self.draw_line(x1, y1, x2, y1, char)  # Top
            self.draw_line(x1, y2, x2, y2, char)  # Bottom
            self.draw_line(x1, y1, x1, y2, char)  # Left
            self.draw_line(x2, y1, x2, y2, char)  # Right
    
    def draw_text(self, x, y, text):
        """Draw text at position (x, y)"""
        for i, char in enumerate(text):
            if x + i < self.width:
                self.set_pixel(x + i, y, char)
    
    def get_canvas(self):
        """Return the canvas as a string"""
        return '\n'.join(''.join(row) for row in self.canvas)
    
    def display(self):
        """Display the canvas"""
        print(self.get_canvas())
    
    def save(self, filename):
        """Save canvas to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.get_canvas())
        print(f"Canvas saved to {filename}")


class DrawingCanvas:
    """Graphical drawing canvas using tkinter"""
    
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("AsciiForge - Drawing Canvas")
        
        # Create canvas
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg='black', cursor='cross')
        self.canvas.pack(side=tk.TOP)
        
        # Create PIL Image for drawing
        self.image = Image.new('RGB', (width, height), 'black')
        self.draw = ImageDraw.Draw(self.image)
        
        # Drawing state
        self.old_x = None
        self.old_y = None
        self.pen_color = 'white'
        self.pen_width = 3
        
        # Bind mouse events
        self.canvas.bind('<Button-1>', self.start_draw)
        self.canvas.bind('<B1-Motion>', self.draw_line)
        self.canvas.bind('<ButtonRelease-1>', self.stop_draw)
        
        # Create control panel
        self.create_controls()
        
        # ASCII characters for conversion (from darkest to lightest)
        self.ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.', ' ']
        
    def create_controls(self):
        """Create control buttons"""
        control_frame = tk.Frame(self.root)
        control_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5)
        
        # Clear button
        clear_btn = tk.Button(control_frame, text="Clear", command=self.clear_canvas)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Pen width controls
        tk.Label(control_frame, text="Pen Size:").pack(side=tk.LEFT, padx=5)
        
        for size in [1, 3, 5, 8, 12]:
            btn = tk.Button(control_frame, text=str(size), width=3,
                          command=lambda s=size: self.set_pen_width(s))
            btn.pack(side=tk.LEFT, padx=2)
        
        # Convert and save button
        convert_btn = tk.Button(control_frame, text="Convert to ASCII & Save", 
                               command=self.convert_and_save, bg='lightgreen')
        convert_btn.pack(side=tk.RIGHT, padx=5)
        
        # Preview button
        preview_btn = tk.Button(control_frame, text="Preview ASCII", 
                               command=self.preview_ascii, bg='lightblue')
        preview_btn.pack(side=tk.RIGHT, padx=5)
    
    def start_draw(self, event):
        """Start drawing"""
        self.old_x = event.x
        self.old_y = event.y
    
    def draw_line(self, event):
        """Draw line as mouse moves"""
        if self.old_x and self.old_y:
            # Draw on canvas
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                   width=self.pen_width, fill=self.pen_color,
                                   capstyle=tk.ROUND, smooth=True)
            
            # Draw on PIL image
            self.draw.line([self.old_x, self.old_y, event.x, event.y],
                          fill=self.pen_color, width=self.pen_width)
            
            self.old_x = event.x
            self.old_y = event.y
    
    def stop_draw(self, event):
        """Stop drawing"""
        self.old_x = None
        self.old_y = None
    
    def clear_canvas(self):
        """Clear the canvas"""
        self.canvas.delete("all")
        self.image = Image.new('RGB', (self.width, self.height), 'black')
        self.draw = ImageDraw.Draw(self.image)
    
    def set_pen_width(self, width):
        """Set pen width"""
        self.pen_width = width
    
    def image_to_ascii(self, img, new_width=100):
        """Convert image to ASCII art"""
        # Convert to grayscale
        img = img.convert('L')
        
        # Resize image
        width, height = img.size
        aspect_ratio = height / width
        new_height = int(aspect_ratio * new_width * 0.55)  # 0.55 to adjust for character aspect ratio
        img = img.resize((new_width, new_height))
        
        # Convert pixels to ASCII
        pixels = img.getdata()
        ascii_str = ""
        
        for i, pixel in enumerate(pixels):
            # Map pixel brightness to ASCII character
            ascii_str += self.ascii_chars[pixel // 25]
            
            # Add newline at end of row
            if (i + 1) % new_width == 0:
                ascii_str += '\n'
        
        return ascii_str
    
    def preview_ascii(self):
        """Preview ASCII art in a new window"""
        ascii_art = self.image_to_ascii(self.image)
        
        # Create preview window
        preview_window = tk.Toplevel(self.root)
        preview_window.title("ASCII Art Preview")
        
        # Create text widget with scrollbar
        frame = tk.Frame(preview_window)
        frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_widget = tk.Text(frame, wrap=tk.NONE, 
                             yscrollcommand=scrollbar.set,
                             font=('Courier', 8),
                             bg='black', fg='white')
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)
        
        text_widget.insert('1.0', ascii_art)
        text_widget.config(state=tk.DISABLED)
    
    def convert_and_save(self):
        """Convert drawing to ASCII and save"""
        # Ask for filename
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Save ASCII Art"
        )
        
        if filename:
            ascii_art = self.image_to_ascii(self.image)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(ascii_art)
            
            messagebox.showinfo("Success", f"ASCII art saved to {filename}")
            print(f"ASCII art saved to {filename}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


def interactive_canvas():
    """Launch the graphical drawing canvas"""
    print("\nLaunching drawing canvas...")
    print("Instructions:")
    print("- Draw with your mouse by clicking and dragging")
    print("- Use the pen size buttons to change brush size")
    print("- Click 'Clear' to erase everything")
    print("- Click 'Preview ASCII' to see the ASCII version")
    print("- Click 'Convert to ASCII & Save' to save your artwork")
    print("\nClose the window to return to the main menu.\n")
    
    canvas = DrawingCanvas()
    canvas.run()
    
    return canvas


if __name__ == "__main__":
    interactive_canvas()