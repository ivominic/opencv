"""Detekcija lica. Prethodno bilo potrebno instalirati dvije biblioteke:
pip3 install cmake
pip3 install face_recognition
obavezno ovim redom"""
import os
from PIL import Image
import face_recognition
import cv2

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(ROOT_DIR, "fajlovi/lica.jpg")
IMAGE = cv2.imread(IMAGE_PATH)

cv2.imshow("Original", IMAGE)
cv2.waitKey(2000)

# Nalazi sva lica na slici, korišćenjem biblioteke
FACE_LOCATIONS = face_recognition.face_locations(IMAGE)

# printing the number of items in the array
print("Na slici se nalazi {} lica.".format(len(FACE_LOCATIONS)))

for face_location in FACE_LOCATIONS:

    # print lokacije svakog lica (pravouganik)
    top, right, bottom, left = face_location
    print("Lice na lokaciji Top: {}, Left: {}, Bottom: {}, Right: {}".format(
        top, left, bottom, right))

    cv2.rectangle(IMAGE, (left, bottom), (right, top), (0, 250, 0), 2)

    # Svako od nađenih lica prikazuje kao posebnu sliku
    # Ovaj prikaz u posebnim slikama ne radi!!!!
    #face_image = IMAGE[top:bottom, left:right]
    #pil_image = Image.fromarray(face_image)
    # pil_image.show()

cv2.imshow("Iscrtano", IMAGE)
cv2.waitKey(5000)
