"""Čita tekst sa slike"""
import os
from PIL import Image
import pytesseract
import cv2


IMAGE = cv2.imread(
    "/home/ivo/Development/python/opencv/opencv/fajlovi/ocr2.png")

cv2.imshow("Original", IMAGE)
cv2.waitKey(2000)

GRAY = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", GRAY)
cv2.waitKey(2000)

# check to see if we should apply thresholding to preprocess the
# image
GRAY = cv2.threshold(GRAY, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove
# noise

GRAY = cv2.medianBlur(GRAY, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
FILENAME = "{}.png".format(os.getpid())
cv2.imwrite(FILENAME, GRAY)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
TEXT = pytesseract.image_to_string(Image.open(FILENAME))
os.remove(FILENAME)
print(TEXT)

# show the output images
# cv2.imshow("Image", image)
cv2.imshow("Output", GRAY)
cv2.waitKey(2000)

# USAGE
# python3 ocr.py --image ../opencv/example_01.png
# python3 ocr.py --image ../opencv/example_02.png  --preprocess blur
