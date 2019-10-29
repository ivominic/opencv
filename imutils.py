"""Biblioteka koja će se importovati za rad sa slikama"""
import numpy as np
import cv2


def translate(image, x_osa, y_osa):
    """Metoda koja translira sliku po x i y osi.
    Pozitivne vrijednosti desno i dolje, negativne lijevo i gore"""
    matrica = np.float32([[1, 0, x_osa], [0, 1, y_osa]])
    shifted = cv2.warpAffine(
        image, matrica, (image.shape[1], image.shape[0]))
    return shifted


def rotate(image, angle, center=None, scale=1.0):
    """ Metoda koja rotira sliku oko centra"""
    (height, width) = image.shape[:2]

    if center is None:
        center = (width // 2, height // 2)

    matrica = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, matrica, (width, height))
    return rotated


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    """ Vrši resize fotografije"""
    dim = None
    (pom_height, pom_width) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        radius = height/float(pom_height)
        dim = (int(pom_width * radius), height)
    else:
        radius = width/float(pom_width)
        dim = (width, int(pom_height * radius))

    resized = cv2.resize(image, dim, interpolation=inter)
    return resized
