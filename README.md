# Live-Stream-Face-Recognition-System
A real-time facial recognition application using Python, OpenCV, and `face_recognition` library with a simple Tkinter GUI.   This system captures live video from your webcam, recognizes faces based on a pre-trained set of images, and logs recognized faces with timestamps to a CSV file.  

## Features

- Real-time face detection and recognition from webcam feed.
- Recognition against a folder of known faces (images in `TrainingImages`).
- Records recognized faces with date and time in `records.csv`.
- Simple GUI interface to start/stop recognition and exit the app.
- Lightweight and easy to set up with Python.

## Table of Contents

- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [How It Works](#how-it-works)  
- [Requirements](#requirements)  
- [Notes and Tips](#notes-and-tips)  

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/live-stream-facial-recognition.git
   cd live-stream-facial-recognition
   
3. (Optional) Create and activate a virtual environment:
   ```bash
    python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate

5. Install the dependencies:
   ```bash
   pip install -r requirements.txt

# Usage

1. Add images of known individuals to the TrainingImages folder.
   - Name the images as the person's name, e.g., john_doe.jpg.
     
3. Run the program:
   ```bash
     python main.py
   
4. The GUI window will open:
   - Click Start Recognition to start the webcam and face recognition.
   - Press the q key in the webcam window to stop the live stream.
   - Click Close in the GUI to exit the program.
     
5. Recognized faces and the timestamp will be logged automatically in records.csv.

# Project Structure
<pre>
live-stream-face-recognition-system/
│
├── TrainingImages/          # Folder to store known face images
│   ├── person1.jpg
│   ├── person2.jpg
│   └── ...
├── main.py                  # Main application code and GUI
├── utils.py                 # Helper functions (encoding, logging)
├── requirements.txt         # Python dependencies
├── records.csv              # Automatically generated log file
├── README.md                # This file
└── __init__.py              # Marks the project folder as a package (optional)
</pre>
  
# How It Works 
- Loading Known Faces:
The system loads and encodes face images from TrainingImages/.
- Face Recognition:
Using face_recognition and OpenCV, the system compares faces detected from the webcam live stream against the known faces.
- Logging:
When a face is recognized, the person's name and the date/time are logged to records.csv.
- GUI:
A simple Tkinter GUI provides buttons to start recognition and close the app gracefully.

# Requirements
- Python 3.6+
- OpenCV (opencv-python)
- face_recognition
- numpy
- Tkinter (usually included with Python)

# Notes and Tips
- Ensure good lighting conditions for accurate face recognition.
- Webcam feed can be closed by pressing the q key (make sure Caps Lock is off).
- The Close button in the GUI exits the whole application.
- Add clear, front-facing images in the TrainingImages folder with the filename as the person's name.
- This project is meant for educational and demonstration purposes; for production use, additional optimizations and security considerations are necessary.
