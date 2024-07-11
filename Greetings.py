import streamlit as st
import cv2
import numpy as np
import time

# Initialize session state to store start time
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()  # Automatically start timing when the app loads

# Display the start time
st.write("Timing started...")

# Function to detect face and return a frame with the greeting
def detect_face_and_greet(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained face detector model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If faces are detected, draw a rectangle around the first face and add greeting text
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (245, 246, 252), 2)
        cv2.putText(frame, "Hola Visitor :D!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (100, 255, 100), 2)

    return frame

# Button to start webcam
col1, col2 = st.columns(2)
start_button = col1.button("Start Webcam")
stop_button = col2.button("Stop Webcam")

end_time = time.time()
time_delay = end_time - st.session_state.start_time
st.write(f"Time delay: {time_delay:.2f} seconds")

# Open webcam
cap = cv2.VideoCapture(0)

stframe = st.empty()  # Placeholder for the video frame

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        st.write("Failed to capture image")
        break

    # Detect face and add greeting
    frame = detect_face_and_greet(frame)

    # Convert frame to RGB (required for displaying in Streamlit)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the frame
    stframe.image(frame, channels="RGB")

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

    # Check if 10 seconds have passed
    if time.time() - st.session_state.start_time > 1:
        break

# Release the webcam
cap.release()
cv2.destroyAllWindows()
