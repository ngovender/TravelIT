
# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os


# load the example image and convert it to grayscale_sampled
#image = cv2.imread('/Users/natashagovender/TravelIt/images/openCV/IMG_2797_altered.jpg')
image = cv2.imread('/Users/natashagovender/TravelIt/images/IMG_2_cropped_sampled.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)


# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

# show the output images
#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
#cv2.waitKey(0)