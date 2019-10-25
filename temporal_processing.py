#  Name: Clyde Sumagang and Roy Morla
#  Date: October 1, 2019
#  Course: CST205
#  Description: This code will remove unwanted things in images via temporal processing.

#  Summary: This probelm was a little more difficult, however, we were able to
#  find the median of all the images by storing each RGB value into its
#  own list and finding the median of those. It took awhile, but walking through it on paper
#  really helped, and we were able to figure out how we should loop through it.

import glob
from PIL import Image


def temporal_processing(im):
    all_pixels = []
    new_image = []
    red = []  # Individual lists for each RGB channel.
    green = []
    blue = []

    middle = (len(im)//2)  # The middle is calculated by the floor division of the amount of images

    for i in im:  # The image data is then stored into a list
        all_pixels.append(list(i.getdata()))

    for pixel in range(len(all_pixels[0])):  # Since all images are the same size, we can use the length of the first image.
        for indi in range(len(all_pixels)):  # We then loop through the 11 different images and append the RGB values into their respective
            red.append(all_pixels[indi][pixel][0])
            green.append(all_pixels[indi][pixel][1])
            blue.append(all_pixels[indi][pixel][2])
        red.sort()
        green.sort()
        blue.sort()
        new_image.append((red[middle], green[middle], blue[middle]))  # This appends the median of all RGB lists into the new_image list as a tuple.
        red.clear()  # We then have to clear the lists to avoid bad data.
        green.clear()
        blue.clear()
    return new_image


images = glob.glob('images/*')  # This will get all files from the images directory
im = []
for imgs in images:  # We store the open images into im list
    im.append(Image.open(imgs))

new_image = temporal_processing(im)
canvas = Image.new('RGB', im[0].size)  # We can use the first image for size because theyre all the same size.
canvas.putdata(new_image)
canvas.save("clean_image.png")
canvas.show()
