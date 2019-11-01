"""Mask slike"""
import cv2
import numpy as np

IMAGE = cv2.imread(
    "/home/ivo/Development/python/opencv/opencv/fajlovi/slika1.jpeg")

# učitavanje slike u matricu (numpy array)
cv2.imshow("Original", IMAGE)
cv2.waitKey(2000)

# Kreiranje crne matrice u dimenzijama slike i bijeli prozor

MASK = np.zeros(IMAGE.shape[:2], dtype="uint8")
(C_X, C_Y) = (IMAGE.shape[1] // 2, IMAGE.shape[0] // 2)
cv2.rectangle(MASK, (C_X - 75, C_Y - 75), (C_X + 75, C_Y + 75), 255, -1)
cv2.imshow("Mask kvadrat", MASK)
cv2.waitKey(2000)

MASKED = cv2.bitwise_and(IMAGE, IMAGE, mask=MASK)
cv2.imshow("Mask kvadrat slika", MASKED)
cv2.waitKey(2000)

# Kreiranje crne matrice u dimenzijama slike i bijeli krug
MASK = np.zeros(IMAGE.shape[:2], dtype="uint8")
(C_X, C_Y) = (IMAGE.shape[1] // 2, IMAGE.shape[0] // 2)
cv2.circle(MASK, (C_X, C_Y), 100, 255, -1)
cv2.imshow("Mask krug", MASK)
cv2.waitKey(2000)

MASKED = cv2.bitwise_and(IMAGE, IMAGE, mask=MASK)
cv2.imshow("Mask krug slika", MASKED)
cv2.waitKey(2000)
