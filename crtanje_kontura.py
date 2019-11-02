"""Iscrtavanje kontura i broj objekata"""
import cv2
IMAGE = cv2.imread(
    "/home/ivo/Development/python/opencv/opencv/fajlovi/coins.jpg")

cv2.imshow("Original", IMAGE)
cv2.waitKey(2000)

GRAY = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2GRAY)

# gaussian blurring - indeks povećan na 19, da bi čistije konture bile
BLURRED = cv2.GaussianBlur(GRAY, (19, 19), 0)
cv2.imshow("Gaussian blurr", BLURRED)
cv2.waitKey(2000)

CANNY = cv2.Canny(BLURRED, 30, 150)
cv2.imshow("Detektovane ivice", CANNY)
cv2.waitKey(2000)

# Prva promjenljiva koju f-ja vraća je broj kontura, druga nas ne interesuje
# Koristi kopiju slike jer se slika trajno uništava
(CNTS, _) = cv2.findContours(CANNY.copy(),
                             cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Broj kontura/objekata na slici je : {}".format(len(CNTS)))

# Koristi kopiju slike jer se slika trajno uništava iscrtavanjem
COINS = IMAGE.copy()

# iscrtava konture zelenom bojom, debljine 2, na originalnoj slici
# -1 označava da se prikazuje unutrašnjost konture - ovo nisam baš siguran
cv2.drawContours(COINS, CNTS, -1, (0, 255, 0), 2)
cv2.imshow("Kontura", COINS)
cv2.waitKey(2000)
