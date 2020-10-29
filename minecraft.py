from mcpi.minecraft import Minecraft
from mcpi import block
import time
from json import load
from os import remove
from imgprep import *


def drawing(image, start_in=(0, 0, 0)):
    start_x, start_y, start_z = start_in
    for y, row in enumerate(image):
        for x, index in enumerate(row):
            mc.setBlock(x + start_x, y + start_y, start_z, 35, index)


mc = Minecraft.create()

Tk().withdraw()
filename = askopenfilename()

print('Opening file...')

img = cv2.imread(filename)

print('Resizing...')

img_resized = resize(img)

print('Reshaping....')

img_reshaped = reshape(img_resized)

print('Drawing!')

drawing(img_reshaped)

print('The end.')