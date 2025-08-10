import tkinter as tk
import numpy as np
import cv2
import os
import face_recognition
from utils import get_face_encodings, document_recognised_face

# Initialize lists for images and labels
known_faces = []
face_labels = []

# Load training images
image_files = os.listdir("TrainingImages")
for image_name in image_files:
    current_image = cv2.imread(f'TrainingImages/{image_name}')
    known_faces.append(current_image)
    face_labels.append(os.path.splitext(image_name)[0])

# Encode known faces
known_face_encodings = get_face_encodings(known_faces)

# Function to start recognition
def start_recognition_program():
    video_capture = cv2.VideoCapture(0)  # 0 for internal webcam, 1 for external

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        resized_frame = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(resized_frame)
        current_face_encodings = face_recognition.face_encodings(resized_frame, face_locations)

        for face_encoding, location in zip(current_face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                recognized_name = face_labels[best_match_index].upper()
                top, right, bottom, left = location
                top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, recognized_name, (left + 6, bottom - 6),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                document_recognised_face(recognized_name)

        cv2.imshow("Webcam", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


# Tkinter GUI
root = tk.Tk()
root.title("Live Stream Facial Recognition System")

label = tk.Label(root, text="Click the button to start the facial recognition program")
label.pack(pady=10)

start_button = tk.Button(root, text="Start Recognition", command=start_recognition_program)
start_button.pack(pady=10)

def quit_app():
    root.quit()
    cv2.destroyAllWindows()

exit_button = tk.Button(root, text="Close", command=quit_app)
exit_button.pack(pady=10)

root.mainloop()
