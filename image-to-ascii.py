from PIL import Image

def asciiConvert(image_path, image_type, save_path, scale_factor):
    scale_factor = int(scale_factor)

    # Open and get image size
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print("Error: Image file not found.")
        return
    except Exception as e:
        print(f"Error: Unable to open image - {e}")
        return

    width, height = img.size

    # Resize image (downscale)
    resized_img = img.resize((width // scale_factor, height // scale_factor))
    resized_img.save(f"resized.{image_type}")

    # Open resized image
    resized_img = Image.open(f"resized.{image_type}")
    width, height = resized_img.size

    # Map pixels to ASCII characters based on luminance
    ascii_chars = '@%#*+=-:. '

    ascii_art = ""
    for y in range(height):
        for x in range(width):
            pixel = resized_img.getpixel((x, y))
            luminance = sum(pixel) / 3  # Calculate luminance
            ascii_index = int((luminance / 255) * (len(ascii_chars) - 1))
            ascii_art += ascii_chars[ascii_index]
        ascii_art += '\n'

    # Save ASCII art to file
    with open(save_path, "w") as f:
        f.write(ascii_art)

if __name__ == '__main__':
    asciiConvert("random.jpg", "jpg", "random.txt", "3")
# Change random.jpg ^, to the name of your own image
