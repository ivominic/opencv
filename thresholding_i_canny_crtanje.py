"""Trešholding - sve ispod neke vrijednosti u 0, sve iznad u 255 = crno-bijela slika
Iscrtavanje kontura Canny metoda"""
import cv2
IMAGE = cv2.imread(
    "/home/ivo/Development/python/opencv/opencv/fajlovi/coins.jpg")

cv2.imshow("Original", IMAGE)
cv2.waitKey(2000)

GRAY = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2GRAY)

# gaussian blurring
BLURRED = cv2.GaussianBlur(GRAY, (5, 5), 0)
cv2.imshow("Gaussian blurr", BLURRED)
cv2.waitKey(2000)

# simple treshold, parametri: slika, granica, gornja vrijednost, metod trasholdinga
(T, THRESH) = cv2.threshold(BLURRED, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("THRESHold Binary", THRESH)
cv2.waitKey(2000)

# simple THRESHolding using inv binary
(T, THRESH_INVERZNO) = cv2.threshold(BLURRED, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("THRESHold Inv Binary", THRESH_INVERZNO)
cv2.waitKey(2000)
cv2.imshow("Maskirano", cv2.bitwise_and(IMAGE, IMAGE, mask=THRESH_INVERZNO))
cv2.waitKey(2000)
# adaptive THRESHolding using mean
THRESH = cv2.adaptiveThreshold(
    BLURRED, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Adaptive mean", THRESH)
cv2.waitKey(2000)
# adaptive THRESHolding using gaussian
THRESH = cv2.adaptiveThreshold(
    BLURRED, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Adaptive gaussian", THRESH)
cv2.waitKey(2000)

# Crtanje ivica
CANNY = cv2.Canny(BLURRED, 30, 150)
cv2.imshow("Canny Edge Detected", CANNY)
cv2.waitKey(3000)
