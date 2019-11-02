"""Blurovanje slike na nekoliko načina"""
import cv2
import numpy as np

IMAGE = cv2.imread(
    "/home/ivo/Development/python/opencv/opencv/fajlovi/slika1.jpeg")

cv2.imshow("Original", IMAGE)
cv2.waitKey(2000)

# average blurring
BLURRED = np.hstack([
    cv2.blur(IMAGE, (3, 3)),
    cv2.blur(IMAGE, (5, 5)),
    cv2.blur(IMAGE, (7, 7))])

cv2.imshow("averaged blurr", BLURRED)
cv2.waitKey(2000)

# gaussian blurring
BLURRED = np.hstack([
    cv2.GaussianBlur(IMAGE, (3, 3), 0),
    cv2.GaussianBlur(IMAGE, (5, 5), 0),
    cv2.GaussianBlur(IMAGE, (7, 7), 0)])

cv2.imshow("Gaussian blurr", BLURRED)
cv2.waitKey(2000)

# median blurring
BLURRED = np.hstack([
    cv2.medianBlur(IMAGE, 3),
    cv2.medianBlur(IMAGE, 5),
    cv2.medianBlur(IMAGE, 7)])

cv2.imshow("Median blurr", BLURRED)
cv2.waitKey(2000)

# bilateral blurring
BLURRED = np.hstack([
    cv2.bilateralFilter(IMAGE, 3, 21, 21),
    cv2.bilateralFilter(IMAGE, 5, 31, 31),
    cv2.bilateralFilter(IMAGE, 7, 41, 41)])

cv2.imshow("bilateral blurr", BLURRED)
cv2.waitKey(2000)
