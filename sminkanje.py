"""Dodavanje šminke na lice"""
import face_recognition
from PIL import Image, ImageDraw

# Učitavanje slika u numpy niz/matricu
IMAGE = face_recognition.load_image_file("fajlovi/popaj.jpg")

# Prepoznavanje djelova lica
DJELOVI_LICA = face_recognition.face_landmarks(IMAGE)

print(DJELOVI_LICA)

for face_landmarks in DJELOVI_LICA:
    pil_image = Image.fromarray(IMAGE)
    d = ImageDraw.Draw(pil_image, 'RGBA')
    # RGBA - dodavanje alfa komposita (rgbA), da bude kao providno

    # popunjavanje poligona i ivice za obrve
    d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
    d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
    d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
    d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

    # Popunjavanje poigona i ivice za usne
    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    # Crveni providni fill za oči
    d.polygon(face_landmarks['left_eye'], fill=(255, 0, 0, 30))
    d.polygon(face_landmarks['right_eye'], fill=(255, 0, 0, 30))

    # Trepavice
    d.line(face_landmarks['left_eye'] +
           [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
    d.line(face_landmarks['right_eye'] +
           [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

    pil_image.show()

    # Čuvanje slike, pošto prikaz nešto ne radi
    pil_image.save("fajlovi/nasminkan.jpg")
