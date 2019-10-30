"""Aritmetičke operacije nad slikom"""
import argparse  # biblioteka za parsiranje argumenata iz komandne linije
import numpy as np
import cv2  # OpenCV biblioteka

# Čitanje argumenata iz komandne linije i njihovo smještanje u dictionary
AP = argparse.ArgumentParser()
AP.add_argument("-i", "--IMAGE", required=True,
                help="/home/ivo/Development/python/opencv/opencv/fajlovi/slika1.jpeg")
ARGS = vars(AP.parse_args)

# Učitavanje slike sa putanje sa diska. Pošto se slika na ovaj način čuva kao NumPy niz (matrica)
# mogu se dobiti podaci o:
# širini slike, visini slike i broju kanala (3 maksimalno - red, green, blue)
IMAGE = cv2.imread(
    "/home/ivo/Development/python/opencv/opencv/fajlovi/slika1.jpeg")

cv2.imshow("Original", IMAGE)
cv2.waitKey(1000)

# cv2 sve preko 255 tretirao kao 255, sve manje od 0 kao nulu, kad sabira uint8
print("max of 255 by cv2: {}".format(
    cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0 by cv2: {}".format(
    cv2.subtract(np.uint8([50]), np.uint8([100]))))

# np radi mod 255, samo počinje da broji od 0, pa bude za 1 manje od matematičkog
print("wrap of max by np: {}".format(np.uint8([200])+np.uint8([100])))
print("wrap of min by np: {}".format(np.uint8([50])-np.uint8([100])))


# generating one array and multiplying it with 100
# adding that array to the actual IMAGE numpy array
MATRICA = np.ones(IMAGE.shape, dtype="uint8") * 100
SABRANO = cv2.add(IMAGE, MATRICA)
cv2.imshow("SABRANO IMAGE", SABRANO)
cv2.waitKey(3000)

# generating one array and multiplying it with 50
# substracting that array to the actual IMAGE numpy array
MATRICA = np.ones(IMAGE.shape, dtype="uint8") * 50
ODUZETO = cv2.subtract(IMAGE, MATRICA)
cv2.imshow("ODUZETO IMAGE", ODUZETO)
cv2.waitKey(3000)
