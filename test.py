""" Transformacije slike"""
import argparse  # biblioteka za parsiranje argumenata iz komandne linije
import cv2  # OpenCV biblioteka
import imutils  # lokalni fajl/biblioteka imutils.py

# Čitanje argumenata iz komandne linije i njihovo smještanje u dictionary
AP = argparse.ArgumentParser()
AP.add_argument("-i", "--image", required=True,
                help="/home/ivo/Development/python/opencv/opencv/fajlovi/slika1.jpeg")
ARGS = vars(AP.parse_args)

# Učitavanje slike sa putanje sa diska. Pošto se slika na ovaj način čuva kao NumPy niz (matrica)
# mogu se dobiti podaci o:
# širini slike, visini slike i broju kanala (3 maksimalno - red, green, blue)
IMAGE = cv2.imread(
    "/home/ivo/Development/python/opencv/opencv/fajlovi/slika1.jpeg")
# IMAGE = cv2.imread(ARGS["image"])

# Pomjera sliku dolje
SHIFTED = imutils.translate(IMAGE, 0, 100)
cv2.imshow("Dolje", SHIFTED)
cv2.waitKey(1000)

# Pomjera sliku gore
SHIFTED = imutils.translate(IMAGE, 0, -100)
cv2.imshow("Gore", SHIFTED)
cv2.waitKey(1000)

# Pomjera sliku lijevo
SHIFTED = imutils.translate(IMAGE, -100, 0)
cv2.imshow("Lijevo", SHIFTED)
cv2.waitKey(1000)

# Pomjera sliku desno
SHIFTED = imutils.translate(IMAGE, 100, 0)
cv2.imshow("Desno", SHIFTED)
cv2.waitKey(1000)

# Pomjera sliku desno dolje
SHIFTED = imutils.translate(IMAGE, 100, 50)
cv2.imshow("Dolje desno", SHIFTED)
cv2.waitKey(1000)
