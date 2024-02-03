#This code captures an image from a webcam, performs number plate recognition, and then facial recognition. If the recognized person is unauthorized, it plays a siren sound, and the user can press 'v' to stop the siren sound.

import cv2
import easyocr
import face_recognition
import pyttsx3
from playsound import playsound
import pygame

# Set the location of the face recognition model
face_recognition.api.face_recognition_model_v1_location = "C:/Python312/Lib/site-packages/face_recognition_models/models/dlib_face_recognition_resnet_model_v1.dat"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
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
    reference_image = face_recognition.load_image_file(
        "C:\\Users\\DELL\\OneDrive\\Desktop\\Smart-Plate-Access-Control\\SPAC\\hugging face\\face1.jpg")
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
    pygame.mixer.init()
    pygame.mixer.music.load(
        "C:\\Users\\DELL\\OneDrive\\Desktop\\Smart-Plate-Access-Control\\SPAC\\hugging face\\Siren.mpeg")
    pygame.mixer.music.play()


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
        # Monitor for 'v' key press to stop the audio
        while True:
            key = input("Press 'v' and hit enter to stop: ")
            if key.lower() == 'v':
                pygame.mixer.music.stop()
                break

else:
    print("Access Denied")
    print("Number plate not recognized or unauthorized.")
