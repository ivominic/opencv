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

# crtanje krugova
cv2.circle(CANVAS, (100, 100), 10, GREEN)
cv2.imshow("Krug u 100, 100 prečnika 10", CANVAS)
cv2.waitKey(1000)

# crtanje koncentričnih krugova prečnika od 0 do 150, sa korakom 25. Clear kanvasa
CANVAS = np.zeros((300, 300, 3), dtype="uint8")
WHITE = (255, 255, 255)
# (CENTER_X, CENTER_Y) = (CANVAS.shape[1]//2, CANVAS.shape[0]//2)
(CENTER_X, CENTER_Y) = (150, 150)

for r in range(0, 175, 25):
    cv2.circle(CANVAS, (CENTER_X, CENTER_Y), r, WHITE)

cv2.imshow("koncentrični krugovi", CANVAS)
cv2.waitKey(1000)


# random generisanje radijusa, centra i boje. -1 označava popunjenu unutrašnjost kruga
CANVAS = np.zeros((300, 300, 3), dtype="uint8")
for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))
    cv2.circle(CANVAS, tuple(pt), radius, color, -1)
cv2.imshow("CANVAS", CANVAS)
cv2.waitKey(5000)
