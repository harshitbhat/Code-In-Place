"""
This program takes an image and generates a reflection.
The top half of the generated image is the same as the original.
The bottom half is the mirror reflection of the top half.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/mt-rainier.jpg'

def make_reflected(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height
    # TODO: your code here.
    reflected = SimpleImage.blank(width, 2*height)
    for x in range(0,width):
        for y in range(0, height):
            pixel = image.get_pixel(x, y)
            reflected.set_pixel(x, y, pixel)
            reflected.set_pixel(x, 2 * height - y - 1, pixel)
    return reflected


def main():
    # Get file and load image
    filename = get_file()

    # Show the original image
    original = SimpleImage(filename)
    original.show()

    # Show the reflected image
    reflected = make_reflected(filename)
    reflected.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()