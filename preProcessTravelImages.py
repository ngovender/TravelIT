
import numpy as np
import argparse
import imutils
import cv2
from PIL import Image, ImageEnhance
import scipy.misc

from scipy import misc
from scipy.misc.pilutil import Image



# load the image from disk
#im = cv2.imread('/Users/natashagovender/TravelIt/images/IMG_12_cropped_sampled.jpg')
#height, width, channels = im.shape
#print(height,width)
#im = cv2.resize(image, (1024, 768))
im = cv2.imread('/Users/natashagovender/TravelIt/images/IMG_2797_cropped_sampled.jpg')

# loop over the rotation angles again, this time ensuring
# no part of the image is cut off
#for angle in np.arange(0, 360, 15):
#rotated = imutils.rotate_bound(im, 90)
#cv2.imshow("Rotated (Correct)", rotated)
#cv2.waitKey(0)

if im is not None:
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    _,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV) # threshold
    thresh = cv2.Canny(gray,40,200)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(2,2))
    dilated = cv2.dilate(thresh,kernel,iterations = 9) # dilate


cv2.imwrite("/Users/natashagovender/TravelIt/images/openCV/IMG_2797_altered.jpg",dilated)