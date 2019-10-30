"""Flip i krop slike"""
import argparse  # biblioteka za parsiranje argumenata iz komandne linije
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

# Flip slike po x osi kada je drugi parametar 1, po y kad je 0, po obje ose kad je -1
cv2.imshow("Original", IMAGE)
cv2.waitKey(1000)

FLIPPED = cv2.flip(IMAGE, 0)
cv2.imshow("Po y osi", FLIPPED)
cv2.waitKey(1000)

FLIPPED = cv2.flip(IMAGE, 1)
cv2.imshow("Po x osi", FLIPPED)
cv2.waitKey(1000)

FLIPPED = cv2.flip(IMAGE, -1)
cv2.imshow("Po obje ose", FLIPPED)
cv2.waitKey(1000)

# kropovanje slike
# start y 15: end y 222 , start x 150: endx 400
KROP = IMAGE[15:222, 150:400]
cv2.imshow("Kropovana slika", KROP)
cv2.waitKey(1000)
