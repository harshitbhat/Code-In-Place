"""
This program loads an image and applies the narok filter
to it by setting "bright" pixels to grayscale values.
"""

from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/simba-sq.jpg')

    for pixel in image:
        average_component = (pixel.red + pixel.green + pixel.blue ) // 3
        if average_component > 153:
            pixel.red = average_component
            pixel.green = average_component
            pixel.blue = average_component
    image.show()

if __name__ == '__main__':
    main()