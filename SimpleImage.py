################################################################################
#
# Description:
#
# This module implements a simple interface to reading and writing digital
# images in a variety of standard formats. It is built on top of the Python
# Imaging Library (PIL) http://www.pythonware.com/products/pil/. The main
# purpose of the module is to help students of The University of Melbourne
# subject COMP10001 "Foundations of Computing" with their project for
# steganography. Images are represented as rectangular
# lists of lists of integers, where each pixel is a 3-tuple of integer
# intensity values in the range [0,255]. The elements of each tuple
# represent the (red, green, blue) colour components, in that order.
#
# Authors:
#
# Bernie Pope (bjpope@unimelb.edu.au)
#
# Date created:
#
# 29 July 2012
#
# Date modified and reason:
#
# 1 Aug 2012:  Converted all input image formats to "L" 8 bit / pixel.
# 5 Aug 2012:  Module comments added. 
# 1 Aug 2013:  Modified code to support colour images (previously was
#              greyscale only).
# 13 Sep 2013: Update code for COMP10001 project 2, semester 2 2013.
#
################################################################################

from PIL import Image

def read_image(filename):
    """read_image(filename) -> list of lists of pixel intensities
    
    Output image is rectangular, RGB, in row major coordinates.
    """
    image = Image.open(filename)
    # Convert image to RGB if it is not already in that format.
    if image.mode != 'RGB':
        image = image.convert('RGB')
    assert(image.mode == 'RGB')
    pixels = list(image.getdata())
    # Convert the flat representation into a list of rows.
    width, height = image.size
    rows_cols = []
    for row in range(height):
        this_row = []
        row_offset = row * width
        for col in range(width):
            this_pixel = pixels[row_offset + col]
            # check that each pixel has (red, green, blue) components only
            if len(this_pixel) != 3:
                raise('Invalid pixel, not in (R,G,B) format: {}'.format(this_pixel))
            r, g, b = this_pixel
            if type(r) != int or type(g) != int or type(b) != int:
                raise('Invalid pixel, intensities are not integers: {}'.format(this_pixel))
            # make sure each intensity value is in the range [0,255]
            r = clip(r)
            g = clip(g)
            b = clip(b)
            this_row.append((r, g, b))
        rows_cols.append(this_row)
    return rows_cols

def clip(n):
    """clip(int) -> int

    Restrict the int argument to the range [0,255]
    """
    return max(0, min(255, n))

def write_image(image, filename):
    """write_image(image, filename) -> None

    Writes image data file to filename.

    Input image must be rectangular, RGB,
    in row major coordinates.
    """
    flat_pixels = []
    for row in image:
        flat_pixels += row
    out_image = Image.new('RGB', (get_width(image), get_height(image)))
    out_image.putdata(flat_pixels)
    out_image.save(filename)

def get_width(image):
    """get_width(image) -> integer width of the image (number of columns).

    Input image must be rectangular list of lists. The width is
    taken to be the length of the first row of pixels. If the image is
    empty, then the width is defined to be 0.
    """
    if len(image) == 0:
        return 0
    else:
        return len(image[0])

def get_height(image):
    """get_height(image) -> integer height of the image (number of rows).

    Input image must be rectangular list of lists. The height is
    taken to be the number of rows.
    """
    return len(image)
