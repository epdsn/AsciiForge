import PIL.Image
import subprocess
import sys
import example
import canvas

print("Welcom to AsciiForge!")
print("You can create ASCII art from images, use predefined ASCII art pieces, or create your own from scratch.")
print("What would you like to do tody?")
print("1. Convert an image to ASCII art")
print("2. View predefined ASCII art pieces")
print("3. Create your own ASCII art")
print("4. Exit")

choice = 0
while choice not in [1, 2, 3, 4]:
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
if choice == 1:
    #import image-to-ascii # import not working in this environment
    subprocess.run([sys.executable, 'image-to-ascii.py'])
elif choice == 2:
    art_names = example.list_art()
    print("Available ASCII art pieces:")
    for name in art_names:
        print(f"- {name}")
    selected_name = input("Enter the name of the ASCII art you want to view: ")
    art = example.get_art(selected_name)
    if art:
        print(art)
    else:
        print("ASCII art not found.")
elif choice == 3:
    canvas.interactive_canvas()
elif choice == 4:
    print("Exiting AsciiForge. Goodbye!")



