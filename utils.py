import os
import cv2
import face_recognition
from datetime import datetime

# Function to get face encodings from a list of images.
def get_face_encodings(images):
    encoding_list = []
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        face_encoding = face_recognition.face_encodings(image)[0]
        encoding_list.append(face_encoding)
    return encoding_list


# Function to document recognized face in CSV
def document_recognised_face(name, filename='records.csv'):
    capture_date = datetime.now().strftime("%Y-%m-%d")

    if not os.path.isfile(filename):
        with open(filename, 'w') as f:
            f.write('Name,Date,Time')

    with open(filename, 'r+') as file:
        lines = file.readlines()
        existing_names = [line.split(",")[0] for line in lines]

        if name not in existing_names:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            file.write(f'\n{name},{capture_date},{current_time}')
