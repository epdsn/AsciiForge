import PIL.Image


ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=100):

    """Resize image maintaining aspect ratio"""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    return image.resize((new_width, new_height))


def grayify(image):

    """Convert image to grayscale"""
    grayscale_image = image.convert('L')
    return grayscale_image

def pixels_to_ascii(image):
    
    """Convert pixels to ASCII characters"""
    pixels = image.getdata()
    characters = ''.join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def main(new_width=100):

    path = input("Enter the path to the image file: \n")
    try :
        image = PIL.Image.open(path)
    except:
        print("Could not open image file. Please check the path and try again.")

    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[i:(i+new_width)] for i in range(0, pixel_count, 100)])

    print(ascii_image)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
    print("ASCII art written to ascii_image.txt")       

main()