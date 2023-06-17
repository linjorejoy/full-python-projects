import face_recognition
import pickle
import json

# image = face_recognition.load_image_file("./face_recog_img/known/Alby.jpg")
# face_locations = face_recognition.face_locations(image)
# print(face_locations)
known_encodings = {}


image_alby = face_recognition.load_image_file("./face_recog_img/known/Alby.jpg")
alby_encoding = face_recognition.face_encodings(image_alby)[0]
known_encodings["Alby"] = pickle.dumps(alby_encoding)

image_anush = face_recognition.load_image_file("./face_recog_img/known/Anush.jpg")
anush_encoding = face_recognition.face_encodings(image_anush)[0]
known_encodings["Anush"] = pickle.dumps(anush_encoding)

image_linjo = face_recognition.load_image_file("./face_recog_img/known/Linjo.jpg")
linjo_encoding = face_recognition.face_encodings(image_linjo)[0]
known_encodings["Linjo"] = pickle.dumps(linjo_encoding)


image_alby_unknown = face_recognition.load_image_file("./face_recog_img/unknown/Alby Unknown.jpg")
alby_unknown_encoding = face_recognition.face_encodings(image_alby_unknown)[0]


# print(known_encodings)

results = face_recognition.compare_faces(
    [
        pickle.loads(known_encodings["Alby"]),
    ],
    alby_unknown_encoding,
)

print(results[0])
# image_alby = face_recognition.load_image_file("./face_recog_img/known/Alby.jpg")
# alby_encoding = face_recognition.face_encodings(image_alby)[0]
# known_encodings["Alby"] = alby_encoding

# image_anush = face_recognition.load_image_file("./face_recog_img/known/Anush.jpg")
# anush_encoding = face_recognition.face_encodings(image_anush)[0]
# known_encodings["Anush"] = anush_encoding

# image_linjo = face_recognition.load_image_file("./face_recog_img/known/Linjo.jpg")
# linjo_encoding = face_recognition.face_encodings(image_linjo)[0]
# known_encodings["Linjo"] = linjo_encoding


# with open("encodings.dat", mode="wb") as file_encodings:
#     pickle.dump(known_encodings, file_encodings)

# with open("encodings.dat", mode="rb") as file_encodings:
#     deserialized_dict = pickle.load(file_encodings)

#     image_alby_unknown = face_recognition.load_image_file("./face_recog_img/unknown/Alby Unknown.jpg")
#     alby_unknown_encoding = face_recognition.face_encodings(image_alby_unknown)[0]

#     results = face_recognition.compare_faces(
#         [deserialized_dict["Alby"], deserialized_dict["Anush"], deserialized_dict["Linjo"]], alby_unknown_encoding
#     )

#     print(results)