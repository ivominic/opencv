"""Gradient detection - prepoznavanje ivica"""
import cv2
import numpy as np

IMAGE = cv2.imread(
    "/home/ivo/Development/python/opencv/opencv/fajlovi/coins.jpg")

cv2.imshow("Original", IMAGE)
cv2.waitKey(2000)

GRAY = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2GRAY)

# laplace gradient detection
LAP = cv2.Laplacian(GRAY, cv2.CV_64F)

# convert back to 8 bit unsigned int
LAP = np.uint8(np.absolute(LAP))
cv2.imshow("Laplace Gradient Detection", LAP)
cv2.waitKey(3000)

# Sobel X and Y
SOBEL_X = cv2.Sobel(GRAY, cv2.CV_64F, 1, 0)
SOBEL_Y = cv2.Sobel(GRAY, cv2.CV_64F, 0, 1)

# convert back to 8 bit unsigned int
SOBEL_X = np.uint8(np.absolute(SOBEL_X))
SOBEL_Y = np.uint8(np.absolute(SOBEL_Y))

SOBEL_UNIJA = cv2.bitwise_or(SOBEL_X, SOBEL_Y)

cv2.imshow("Sobel X", SOBEL_X)
cv2.waitKey(3000)
cv2.imshow("Sobel Y", SOBEL_Y)
cv2.waitKey(3000)
cv2.imshow("Sobel unija", SOBEL_UNIJA)
cv2.waitKey(3000)
