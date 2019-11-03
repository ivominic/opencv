"""Proračun koliko je neko lice na slici daleko/se razlikuje od drugog"""
import face_recognition

# Učitava sliku sa koje prepoznaje lice.
# Pošto znamo da je samo jedno lice, uzimamo index 0
obama_image = face_recognition.load_image_file("fajlovi/obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Kreira spisak poznatih lica
known_face_encodings = [obama_face_encoding]


# Učitava drugu sliku, sa "nepoznatim licem"
unknown_image = face_recognition.load_image_file("fajlovi/obama_unknown.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Izračunava razliku između lica i setuje dozvoljenu razliku (0.6)
face_distances = face_recognition.face_distance(
    known_face_encodings, unknown_face_encoding)

print("Razlika od {:.2} između dva lica ".format(
    face_distances[0]))
print("Za granični index od 0.6 poklapanje je {}".format(
    face_distances[0] < 0.6))
