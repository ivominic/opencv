"""Čita sliku, uzima jedan njen dio, prikazuje ga, a nakon toga prikazuje cijelu sliku sa izmijenjenom bojom dijela"""
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
#IMAGE = cv2.imread(ARGS["IMAGE"])

# Uzima prvi (lijevo, gore = (0,0)) piksel i prikazuje njegove rgb vrijednosti. OpenCV ih čita inverzno - bgr
(b, g, r) = IMAGE[0, 0]
print("Pixel (0,0) ima boju - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Mijenja boju prvog piksela u crvenu i ponovo štampa vijednosti
IMAGE[0, 0] = (0, 0, 255)
(b, g, r) = IMAGE[0, 0]
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))


# Isijeva i prikazuje gornji lijevi ugao slike, 100x100 piksela
CORNER = IMAGE[0:100, 0:100]
cv2.imshow("Corner just sliced", CORNER)
cv2.waitKey(0)

# Mijenja boju odabranog ugla u zelenu
IMAGE[0:100, 0:100] = (0, 255, 0)
cv2.imshow("Promijenjena boja u zelenu", IMAGE)
cv2.waitKey(0)
