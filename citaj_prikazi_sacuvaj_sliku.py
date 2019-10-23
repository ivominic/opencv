"""Uzima sliku sa diska, čuva je i prikazuje"""
import argparse  # biblioteka za parsiranje argumenata iz komandne linije
import cv2  # OpenCV biblioteka

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
print("Širina slike u pikselima je: {}".format(IMAGE.shape[1]))
print("Visina slike u pikselima je: {}".format(IMAGE.shape[0]))
print("Broj kanala u slici je: {}".format(IMAGE.shape[2]))

# Učitava sliku u cv2 window
# waitKey(0) znači čekaj beskonačno - do nekog dugmeta, inače broj milisekundi se tu unosi
# Treći red čuva sliku u jpg formatu
cv2.imshow("Image Title", IMAGE)
cv2.waitKey(0)
cv2.imwrite("fajlovi/newcat.jpg", IMAGE)
