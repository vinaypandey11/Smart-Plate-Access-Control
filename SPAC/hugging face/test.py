""" import cv2
import easyocr
import importlib.resources as pkg_resources
import face_recognition_models
import face_recognition
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
from playsound import playsound

# Set the location of the face recognition model
face_recognition.api.face_recognition_model_v1_location = "C:/Python312/Lib/site-packages/face_recognition_models/models/dlib_face_recognition_resnet_model_v1.dat"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Function to capture image from the webcam
def capture_image_from_webcam():
    cap = cv2.VideoCapture(0)
    print("Press 'c' to capture the image.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow('Webcam Live', frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite('captured_image.jpg', frame)
            print("Image captured.")
            break

    cap.release()
    cv2.destroyAllWindows()
    return 'captured_image.jpg'

# Function for number plate recognition
def recognize_number_plate(image_path):
    # Initialize the EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Perform text recognition
    results = reader.readtext(image_path)

    # Extract only alphanumeric characters (letters and numbers) and combine them
    recognized_text = ''.join(''.join(char for char in result[1] if char.isalnum()) for result in results)

    print(f"Recognized Text: {recognized_text}")

    # Define the specific number plate format (without spaces for comparison)
    desired_number_plate = 'MH16CZ7892'

    # Check if the specific number plate format is present in the recognized text
    return desired_number_plate in recognized_text

def recognize_face(image_path):
    # Load the reference image
    reference_image = face_recognition.load_image_file("C:\\Users\\DELL\\OneDrive\\Desktop\\Smart-Plate-Access-Control\\SPAC\\hugging face\\face.jpg")
    
    # Check if faces are found in the reference image
    reference_face_locations = face_recognition.face_locations(reference_image)
    if not reference_face_locations:
        print("Error: No faces found in the reference image.")
        return False
    
    # Obtain face encodings for the reference image
    reference_face_encoding = face_recognition.face_encodings(reference_image, reference_face_locations)[0]

    # Load the captured image
    captured_image = face_recognition.load_image_file(image_path)
    captured_face_encodings = face_recognition.face_encodings(captured_image)

    # Check if face encodings are found
    if not captured_face_encodings:
        print("Error: No faces found in the captured image.")
        return False

    # Compare each captured face encoding with the reference face encoding
    for captured_face_encoding in captured_face_encodings:
        results = face_recognition.compare_faces([reference_face_encoding], captured_face_encoding)
        
        # Check if the face is a match
        if any(results):
            return True
    
    return False



# Main script
# Capture image from webcam
image_path = capture_image_from_webcam()

# Perform number plate recognition
number_plate_recognition_result = recognize_number_plate(image_path)

if number_plate_recognition_result:
    # If number plate is recognized, proceed with facial recognition
    face_recognition_result = recognize_face(image_path)

    if face_recognition_result:
        print("Welcome, authorized person!")
        speak("Welcome Mister Vinay Pandey")
    else:
        print("Unauthorized person")
        playsound("C:\\Users\\DELL\\OneDrive\\Desktop\\Smart-Plate-Access-Control\\SPAC\\hugging face\\Siren.mpeg")
else:
    print("Access Denied")
    print("Number plate not recognized or unauthorized.") """
    
 

import cv2
import easyocr
import face_recognition
from playsound import playsound
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime

# Set the location of the face recognition model
face_recognition.api.face_recognition_model_v1_location = "C:/Python312/Lib/site-packages/face_recognition_models/models/dlib_face_recognition_resnet_model_v1.dat"

# Flag to control the siren state
siren_playing = False

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Function to capture image from the webcam
def capture_image_from_webcam():
    cap = cv2.VideoCapture(0)
    print("Press 'c' to capture the image.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow('Webcam Live', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            cv2.imwrite('captured_image.jpg', frame)
            print("Image captured.")
            break

    cap.release()
    cv2.destroyAllWindows()
    return 'captured_image.jpg'

# Function for number plate recognition
def recognize_number_plate(image_path):
    reader = easyocr.Reader(['en'])
    results = reader.readtext(image_path)
    recognized_text = ''.join(''.join(char for char in result[1] if char.isalnum()) for result in results)
    print(f"Recognized Text: {recognized_text}")
    desired_number_plate = 'MH16CZ7892'
    return desired_number_plate in recognized_text

# Function for facial recognition
def recognize_face(image_path):
    reference_image = face_recognition.load_image_file("C:\\Users\\DELL\\OneDrive\\Desktop\\Smart-Plate-Access-Control\\SPAC\\hugging face\\face1.jpg")
    reference_face_locations = face_recognition.face_locations(reference_image)
    
    if not reference_face_locations:
        print("Error: No faces found in the reference image.")
        return False

    reference_face_encoding = face_recognition.face_encodings(reference_image, reference_face_locations)[0]

    captured_image = face_recognition.load_image_file(image_path)
    captured_face_locations = face_recognition.face_locations(captured_image)
    
    if not captured_face_locations:
        print("Error: No faces found in the captured image.")
        return False

    captured_face_encoding = face_recognition.face_encodings(captured_image, captured_face_locations)[0]

    results = face_recognition.compare_faces([reference_face_encoding], captured_face_encoding)

    return any(results)

# Function to play the siren
def play_siren():
    global siren_playing
    siren_playing = True
    playsound("C:\\Users\\DELL\\OneDrive\\Desktop\\Smart-Plate-Access-Control\\SPAC\\hugging face\\Siren.mpeg")
    siren_playing = False
    

# Main script
# Capture image from webcam
image_path = capture_image_from_webcam()

# Perform number plate recognition
number_plate_recognition_result = recognize_number_plate(image_path)

if number_plate_recognition_result:
    # If number plate is recognized, proceed with facial recognition
    face_recognition_result = recognize_face(image_path)

    if face_recognition_result:
        print("Welcome, authorized person!")
        speak("Welcome Mister Vinay")
        
    else:
        print("Unauthorized person")
        # Start playing the siren
        play_siren()
        
        # Wait for 'v' key press to stop the siren
        print("Press 'v' to stop the siren.")
        while not siren_playing:
           key = cv2.waitKeyEx(1)
           if key == ord('v') or key == ord('V'):
             break
else:
    print("Access Denied")
    print("Number plate not recognized or unauthorized.")
 