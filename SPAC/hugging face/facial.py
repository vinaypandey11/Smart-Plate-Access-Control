import cv2
import importlib.resources as pkg_resources
import face_recognition_models
import face_recognition

# Set the location of the face recognition model
face_recognition.api.face_recognition_model_v1_location = "C:/Python312/Lib/site-packages/face_recognition_models/models/dlib_face_recognition_resnet_model_v1.dat"

# Load the reference image
reference_image = face_recognition.load_image_file("C:\\Users\\DELL\\OneDrive\\Desktop\\Smart-Plate-Access-Control\\SPAC\\hugging face\\face.jpg")
reference_face_encoding = face_recognition.face_encodings(reference_image)[0]

# Capture video from the default camera (you can adjust the index if you have multiple cameras)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Find all face locations in the current frame
    face_locations = face_recognition.face_locations(frame)
    
    # If faces are detected, compare each face with the reference image
    for face_location in face_locations:
        # Extract face encoding for the current face
        face_encoding = face_recognition.face_encodings(frame, [face_location])[0]

        # Compare the current face with the reference face
        results = face_recognition.compare_faces([reference_face_encoding], face_encoding)

        name = "Matched" if results[0] else "Not Matched"

        # Draw a rectangle around the face
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Display the result
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Print a welcome message if the face is matched
        if results[0]:
            print("Welcome, authorized person!")

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
video_capture.release()
cv2.destroyAllWindows()
