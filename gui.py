import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
import subprocess
import sys
import example
import canvas


class AsciiForgeApp:
    """Main GUI application for AsciiForge"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("AsciiForge - ASCII Art Creator")
        self.root.geometry("700x600")
        self.root.configure(bg='#1e1e1e')
        # currently-selected image path (set via Select Image button)
        self.selected_image_path = None
        
        # Create main container
        self.create_header()
        self.create_button_panel()
        self.create_output_area()
        
    def create_header(self):
        """Create the header section"""
        header_frame = tk.Frame(self.root, bg='#2d2d2d', height=100)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Title
        title_label = tk.Label(
            header_frame,
            text="AsciiForge",
            font=('Arial', 32, 'bold'),
            bg='#2d2d2d',
            fg='#00ff00'
        )
        title_label.pack(pady=(15, 5))
        
        # Subtitle
        subtitle_label = tk.Label(
            header_frame,
            text="Create, View, and Convert ASCII Art",
            font=('Arial', 12),
            bg='#2d2d2d',
            fg='#cccccc'
        )
        subtitle_label.pack()
    
    def create_button_panel(self):
        """Create the button panel"""
        button_frame = tk.Frame(self.root, bg='#1e1e1e')
        button_frame.pack(pady=20)
        
        # Button style configuration
        button_config = {
            'width': 30,
            'height': 2,
            'font': ('Arial', 11, 'bold'),
            'relief': tk.RAISED,
            'bd': 3
        }
        
        # Button 1: Convert Image to ASCII
        btn1 = tk.Button(
            button_frame,
            text="📷 Convert Image to ASCII Art",
            bg='#0078d4',
            fg='white',
            command=self.convert_image,
            **button_config
        )
        btn1.pack(pady=8)

        # Small Select Image button (opens file dialog) and label showing path
        select_btn = tk.Button(
            button_frame,
            text="Select Image...",
            bg='#0b5fa5',
            fg='white',
            command=self.select_image,
            width=20,
            height=1,
            font=('Arial', 9, 'bold'),
            relief=tk.RAISED,
            bd=2
        )
        select_btn.pack(pady=(2, 8))

        # Path display variable and label
        self.selected_path_var = tk.StringVar(value="No image selected")
        path_label = tk.Label(
            button_frame,
            textvariable=self.selected_path_var,
            font=('Arial', 9),
            bg='#1e1e1e',
            fg='#cccccc',
            wraplength=300,
            justify='left'
        )
        path_label.pack(pady=(0, 8))
        
        # Button 2: View Predefined ASCII Art
        btn2 = tk.Button(
            button_frame,
            text="🎨 View Predefined ASCII Art",
            bg='#7c3aed',
            fg='white',
            command=self.view_predefined_art,
            **button_config
        )
        btn2.pack(pady=8)
        
        # Button 3: Create Your Own ASCII Art
        btn3 = tk.Button(
            button_frame,
            text="✏️ Draw ASCII Art (Canvas)",
            bg='#059669',
            fg='white',
            command=self.create_ascii_art,
            **button_config
        )
        btn3.pack(pady=8)
        
        # Button 4: Exit
        btn4 = tk.Button(
            button_frame,
            text="❌ Exit",
            bg='#dc2626',
            fg='white',
            command=self.exit_app,
            **button_config
        )
        btn4.pack(pady=8)
    
    def create_output_area(self):
        """Create the output display area"""
        output_frame = tk.Frame(self.root, bg='#1e1e1e')
        output_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(10, 20))
        
        # Label
        label = tk.Label(
            output_frame,
            text="Output Console:",
            font=('Arial', 10, 'bold'),
            bg='#1e1e1e',
            fg='#cccccc',
            anchor='w'
        )
        label.pack(fill=tk.X, pady=(0, 5))
        
        # Scrolled text widget for output
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            height=12,
            font=('Courier', 9),
            bg='#0d0d0d',
            fg='#00ff00',
            insertbackground='white',
            wrap=tk.WORD
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Clear button
        clear_btn = tk.Button(
            output_frame,
            text="Clear Output",
            command=self.clear_output,
            bg='#4a4a4a',
            fg='white',
            font=('Arial', 9)
        )
        clear_btn.pack(pady=(5, 0))
        
        # Welcome message
        self.write_output("Welcome to AsciiForge!\n")
        self.write_output("Select an option above to get started.\n")
    
    def write_output(self, text):
        """Write text to output area"""
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)
        self.output_text.update()
    
    def clear_output(self):
        """Clear the output area"""
        self.output_text.delete('1.0', tk.END)
    
    def convert_image(self):
        """Convert image to ASCII art"""
        self.write_output("\n=== Image to ASCII Converter ===\n")
        self.write_output("Launching image converter...\n")
        try:
            # If a path was selected, feed it to the converter via stdin so the
            # existing `image-to-ascii.py` script receives the path when it
            # prompts for input. Capture stdout/stderr and display in the UI.
            if self.selected_image_path:
                proc = subprocess.run(
                    [sys.executable, 'image-to-ascii.py'],
                    input=self.selected_image_path + '\n',
                    text=True,
                    capture_output=True
                )
            else:
                proc = subprocess.run([sys.executable, 'image-to-ascii.py'], capture_output=True, text=True)

            # Write process output to the output console
            if proc.stdout:
                self.write_output(proc.stdout + "\n")
            if proc.stderr:
                self.write_output("Errors:\n" + proc.stderr + "\n")
            self.write_output("Image conversion completed.\n")
        except Exception as e:
            self.write_output(f"Error: {str(e)}\n")
            messagebox.showerror("Error", f"Failed to launch image converter: {str(e)}")

    def select_image(self):
        """Open a file dialog to select an image and show its path in the UI"""
        filetypes = [("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All files", "*.*")]
        path = filedialog.askopenfilename(title="Select image to convert", filetypes=filetypes)
        if path:
            self.selected_image_path = path
            # Update the small label in the button panel
            display_path = path if len(path) < 80 else '...' + path[-77:]
            self.selected_path_var.set(display_path)
            self.write_output(f"Selected image: {path}\n")
    
    def view_predefined_art(self):
        """View predefined ASCII art pieces"""
        self.write_output("\n=== Predefined ASCII Art Library ===\n")
        
        # Create a new window for selection
        art_window = tk.Toplevel(self.root)
        art_window.title("Select ASCII Art")
        art_window.geometry("400x500")
        art_window.configure(bg='#2d2d2d')
        
        # Title
        title = tk.Label(
            art_window,
            text="Available ASCII Art Pieces",
            font=('Arial', 14, 'bold'),
            bg='#2d2d2d',
            fg='#00ff00'
        )
        title.pack(pady=10)
        
        # Listbox for art selection
        listbox_frame = tk.Frame(art_window, bg='#2d2d2d')
        listbox_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        listbox = tk.Listbox(
            listbox_frame,
            yscrollcommand=scrollbar.set,
            font=('Arial', 11),
            bg='#1e1e1e',
            fg='#ffffff',
            selectmode=tk.SINGLE,
            height=15
        )
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)
        
        # Populate listbox
        art_names = example.list_art()
        for name in art_names:
            listbox.insert(tk.END, name)
        
        # Display button
        def display_selected():
            selection = listbox.curselection()
            if selection:
                selected_name = listbox.get(selection[0])
                art = example.get_art(selected_name)
                if art:
                    self.clear_output()
                    self.write_output(f"=== {selected_name} ===\n\n")
                    self.write_output(art + "\n")
                    art_window.destroy()
                else:
                    messagebox.showerror("Error", "ASCII art not found.")
            else:
                messagebox.showwarning("Warning", "Please select an ASCII art piece.")
        
        display_btn = tk.Button(
            art_window,
            text="Display Selected Art",
            command=display_selected,
            bg='#7c3aed',
            fg='white',
            font=('Arial', 11, 'bold'),
            width=20,
            height=2
        )
        display_btn.pack(pady=10)
    
    def create_ascii_art(self):
        """Launch the drawing canvas"""
        self.write_output("\n=== ASCII Art Drawing Canvas ===\n")
        self.write_output("Launching drawing canvas window...\n")
        self.write_output("Draw with your mouse and convert to ASCII art!\n")
        try:
            canvas.interactive_canvas()
            self.write_output("Canvas closed.\n")
        except Exception as e:
            self.write_output(f"Error: {str(e)}\n")
            messagebox.showerror("Error", f"Failed to launch canvas: {str(e)}")
    
    def exit_app(self):
        """Exit the application"""
        if messagebox.askokcancel("Exit", "Are you sure you want to exit AsciiForge?"):
            self.write_output("\nExiting AsciiForge. Goodbye!\n")
            self.root.quit()
