""" Iscrtavanje linija i figura po kanvasu"""
import numpy as np
import cv2

# definisanje kanvasa 300x300 sa 8bitnim unsigned integerom
CANVAS = np.zeros((300, 300, 3), dtype="uint8")

# definisanje boje i iscrtavanje linije color
# argumenti su kanvas/slika, početna i krajnja tačka, boja i opciono debljina
# prikaz u cv2 prozoru
GREEN = (0, 255, 0)
cv2.line(CANVAS, (0, 0), (300, 300), GREEN)
cv2.imshow("Linija 1", CANVAS)
cv2.waitKey(1000)

# crvena linija debljine 3
RED = (0, 0, 255)
cv2.line(CANVAS, (0, 0), (300, 300), RED, 3)
cv2.imshow("Linija 2", CANVAS)
cv2.waitKey(1000)

# crtanje pravoguaonika
GREEN = (0, 255, 0)
cv2.rectangle(CANVAS, (10, 10), (60, 60), GREEN)
cv2.imshow("Običan pravougaonik", CANVAS)
cv2.waitKey(1000)

RED = (0, 0, 255)
cv2.rectangle(CANVAS, (10, 10), (60, 60), RED, 3)
cv2.imshow("Pravougaonik debljine 3", CANVAS)
cv2.waitKey(1000)

BLUE = (255, 0, 0)
cv2.rectangle(CANVAS, (10, 10), (60, 60), BLUE, -1)
cv2.imshow("Debljina -1 znači da se oboji unutrašnjost", CANVAS)
cv2.waitKey(1000)
