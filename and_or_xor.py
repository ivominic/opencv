"""Pravi logičke operacije sa slikama"""
import numpy as np
import cv2


# Kreira 300x300 kvadrat i 250x250 bijeli kvadrat unutar njega
KVADRAT = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(KVADRAT, (25, 25), (275, 275), 255, -1)
cv2.imshow("Kvadrat", KVADRAT)
cv2.waitKey(1000)


# Kreira 300x300 matricu (kvadrat) i bijeli krug prečnika 150 unutar njega/nje
KRUG = np.zeros((300, 300), dtype="uint8")
cv2.circle(KRUG, (150, 150), 150, 255, -1)
cv2.imshow("KRUG", KRUG)
cv2.waitKey(1000)

# ogičke operacije
BITWISE_AND = cv2.bitwise_and(KVADRAT, KRUG)
cv2.imshow("AND", BITWISE_AND)
cv2.waitKey(1000)

BITWISE_OR = cv2.bitwise_or(KVADRAT, KRUG)
cv2.imshow("OR", BITWISE_OR)
cv2.waitKey(1000)

BITWISE_XOR = cv2.bitwise_xor(KVADRAT, KRUG)
cv2.imshow("XOR", BITWISE_XOR)
cv2.waitKey(1000)

BITWISE_NOT = cv2.bitwise_not(KVADRAT, KRUG)
cv2.imshow("Not", BITWISE_NOT)
cv2.waitKey(1000)
