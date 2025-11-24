import tkinter as tk
from gui import AsciiForgeApp

def main():
    """Main entry point"""
    root = tk.Tk()
    app = AsciiForgeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()



