"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: smiley face
    :return:blurred smiley face
    Change the original pixel value to the average value of this pixel and its adjacent pixels
    """
    # Todo: create a new blank img that is as big as the original one
    img = SimpleImage("images/smiley-face.png")
    new_img = SimpleImage.blank(img.width, img.height)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            count = 0
            red = 0
            blue = 0
            green = 0

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                left = x
                right = x + 1
                upper = y
                lower = y + 1

            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                left = x - 1
                right = x
                upper = y
                lower = y + 1

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                left = x
                right = x + 1
                upper = y - 1
                lower = y

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                left = x - 1
                right = x
                upper = y - 1
                lower = y
 
            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                left = x - 1
                right = x + 1
                upper = y
                lower = y + 1

            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                left = x - 1
                right = x + 1
                upper = y - 1
                lower = y

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                left = x
                right = x + 1
                upper = y - 1
                lower = y + 1

            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                left = x - 1
                right = x
                upper = y - 1
                lower = y + 1

            else:
                left = x - 1
                right = x + 1
                upper = y - 1
                lower = y + 1

            for i in range(left, right+1):
                for j in range(upper, lower+1):
                    red = red + img.get_pixel(i, j).red
                    blue = blue + img.get_pixel(i, j).blue
                    green = green + img.get_pixel(i, j).green
                    count += 1

            new_img.get_pixel(x, y).red = red/count
            new_img.get_pixel(x, y).blue = blue/count
            new_img.get_pixel(x, y).green = green/count
    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
