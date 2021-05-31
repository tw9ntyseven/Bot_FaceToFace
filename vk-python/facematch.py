import face_recognition
import requests
import image_save
import sys

img1 = sys.argv[1]
img2 = sys.argv[2]

first_file_stream = image_save.download_file(img1, '1.jpg')
first = face_recognition.load_image_file(first_file_stream)
face_encoding = face_recognition.face_encodings(first)
if (len(face_encoding) != 0):
    first_face_encoding = face_encoding[0]
    # second_response = urllib.request.urlopen(img2)
    second_file_stream = image_save.download_file(img2, '2.jpg')
    second = face_recognition.load_image_file(second_file_stream)
    face_encoding = face_recognition.face_encodings(second)

    if (len(face_encoding) != 0):
        second_face_encoding = face_recognition.face_encodings(second)[0]
        # Compare faces
        results = face_recognition.compare_faces([first_face_encoding], second_face_encoding)
        if results[0]:
            print("Один и тот же человек")
        else:
            print("Разные люди")
    else:
        print("Не вижу лицо на второй фотографии, попробуйте отправить другое фото")
else:
    print("Не вижу лицо на первой фотографии, попробуйте отправить другое фото")