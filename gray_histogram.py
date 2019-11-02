"""Plot histograma i equilizer sive slike"""
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE = cv2.imread(
    "/home/ivo/Development/python/opencv/opencv/fajlovi/slika1.jpeg")

cv2.imshow("Original", IMAGE)
cv2.waitKey(2000)

# BGR to GRAY
GRAY = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", GRAY)
cv2.waitKey(2000)

# kreiranje histograma
HIST = cv2.calcHist([GRAY], [0], None, [256], [0, 256])

# Gray image equilizer
EQLZR = cv2.equalizeHist(GRAY)
cv2.imshow("Ekvilizovana", np.hstack([GRAY, EQLZR]))
cv2.waitKey(1000)

# plot the graph
plt.figure()  # Segmentation fault (core dumped) u verziji matplotlib 3.1.1.
plt.title("Grayscale Histogram")
plt.xlabel("bins")
plt.ylabel("No of pixels")
plt.plot(HIST)
plt.xlim([0, 256])

plt.show()

cv2.waitKey(2000)
