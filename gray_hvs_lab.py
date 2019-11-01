"""Prevodi sliku iz RGB u druge color spaces"""
import cv2

IMAGE = cv2.imread(
    "/home/ivo/Development/python/opencv/opencv/fajlovi/slika1.jpeg")

cv2.imshow("BGR Color Space", IMAGE)
cv2.waitKey(2000)

# BGR to GRAY
GRAY = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", GRAY)
cv2.waitKey(2000)

# BGR to HSV
HSV = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", HSV)
cv2.waitKey(2000)

# BGR to LAB
LAB = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", LAB)
cv2.waitKey(2000)
