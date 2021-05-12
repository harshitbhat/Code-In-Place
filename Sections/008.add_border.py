from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/simba-sq.jpg')
    bordered_img = add_border(image, 10)
    bordered_img.show()


def add_border(original_img, border_size):
    """
    This function returns a new SimpleImage which is the same as
    original image except with a black border added around it. The
    border should be border_size many pixels thick.

    Inputs:
        - original_img: The original image to process
        - border_size: The thickness of the border to add around the image

    Returns:
        A new SimpleImage with the border added around original image
    """
    # TODO: your code here
    width = original_img.width
    height = original_img.height


    bordered = original_img
    black = original_img.get_pixel(0,0)

    black.red = 0
    black.green = 0
    black.blue = 0

    for x in range(0,width):
        for y in range(0,border_size):
            bordered.set_pixel(x,y,black)
        for y in range(height - border_size, height):
            bordered.set_pixel(x,y,black)
    
    for y in range(0,height):
        for x in range(0,border_size):
            bordered.set_pixel(x,y,black)
        for x in range(width - border_size, width):
            bordered.set_pixel(x,y,black)
    
    return bordered


if __name__ == '__main__':
    main()