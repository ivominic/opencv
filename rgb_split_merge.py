"""Mask slike"""
import cv2
import numpy as np

IMAGE = cv2.imread(
    "/home/ivo/Development/python/opencv/opencv/fajlovi/slika1.jpeg")

# učitavanje slike u matricu (numpy array)
cv2.imshow("Original", IMAGE)
cv2.waitKey(2000)

# split slike po chanels - inverzno, jer cv2 čuva RGB kao BGR
(B, G, R) = cv2.split(IMAGE)

cv2.imshow("Red", R)
cv2.waitKey(2000)
cv2.imshow("Green", G)
cv2.waitKey(2000)
cv2.imshow("Blue", B)
cv2.waitKey(2000)


# prikaz boje, ne samo bijela boja
ZEROS = np.zeros(IMAGE.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([ZEROS, ZEROS, R]))
cv2.waitKey(2000)
cv2.imshow("Green", cv2.merge([ZEROS, G, ZEROS]))
cv2.waitKey(2000)
cv2.imshow("Blue", cv2.merge([B, ZEROS, ZEROS]))
cv2.waitKey(2000)

# ponovni merge - originalna slika
MERGED = cv2.merge([B, G, R])
cv2.imshow("spojena", MERGED)
cv2.waitKey(2000)
