# # # import cv2
# # # import easyocr

# # # def capture_image_from_webcam():
# # #     # Initialize the webcam
# # #     cap = cv2.VideoCapture(0)

# # #     while True:
# # #         # Capture frame-by-frame
# # #         ret, frame = cap.read()

# # #         if not ret:
# # #             print("Failed to grab frame")
# # #             break

# # #         # Display the resulting frame
# # #         cv2.imshow('Webcam Live', frame)

# # #         # Wait for the 'c' key to be pressed to capture the image
# # #         if cv2.waitKey(1) & 0xFF == ord('c'):
# # #             print("Capturing image...")
# # #             # Save the captured image
# # #             cv2.imwrite('captured_image.jpg', frame)
# # #             break

# # #     # When everything done, release the capture
# # #     cap.release()
# # #     cv2.destroyAllWindows()

# # #     return 'captured_image.jpg'

# # # def read_number_plate(image_path):
# # #     # Read the image using OpenCV
# # #     image = cv2.imread(image_path)

# # #     # Create an EasyOCR reader instance
# # #     reader = easyocr.Reader(['en'])

# # #     # Detect text from the image
# # #     results = reader.readtext(image)

# # #     # Extract and print recognized numbers
# # #     recognized_numbers = []
# # #     for (bbox, text, prob) in results:
# # #         recognized_numbers.append(text)

# # #     # Print the recognized numbers
# # #     print("Recognized Numbers:", recognized_numbers)
# # #     desired_numbers={'MH 16 DF 0608'}
# # #     if check_matching_numbers(recognized_numbers, desired_numbers):
# # #         print("Authorized")
# # #     else:
# # #         print("Unauthorized")

# # # def check_matching_numbers(recognized_numbers, desired_numbers):
# # #     # Check if any recognized number matches with desired numbers
# # #     for number in recognized_numbers:
# # #         if number in desired_numbers:
# # #             return True
# # #     return False
    

# # # # Capture image from webcam
# # # image_path = capture_image_from_webcam()

# # # # Read number plate from the captured image and display recognized numbers
# # # read_number_plate(image_path)

# # from PIL import Image
# # import face_recognition

# # # Load the jpg file into a numpy array
# # image = face_recognition.load_image_file("C:\\Users\\HP\\Downloads\\SPAC\\face.jpeg")

# # # Find all the faces in the image using the default HOG-based model.
# # # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# # # See also: find_faces_in_picture_cnn.py
# # face_locations = face_recognition.face_locations(image)

# # print("I found {} face(s) in this photograph.".format(len(face_locations)))

# # for face_location in face_locations:

# #     # Print the location of each face in this image
# #     top, right, bottom, left = face_location
# #     print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

# #     # You can access the actual face itself like this:
# #     face_image = image[top:bottom, left:right]
# #     pil_image = Image.fromarray(face_image)
# #     pil_image.show()

# import face_recognition
# known_image = face_recognition.load_image_file("biden.jpg")
# unknown_image = face_recognition.load_image_file("unknown.jpg")

# biden_encoding = face_recognition.face_encodings(known_image)[0]
# unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

import cv2
import importlib.resources as pkg_resources
import face_recognition_models
import face_recognition
face_recognition.api.face_recognition_model_v1_location = "C:/Python312/Lib/site-packages/face_recognition_models/models/dlib_face_recognition_resnet_model_v1.dat"
# face_recognition.api.face_recognition_model_v2_location = "C:\\Python312\\Lib\\site-packages\\face_recognition_models"
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

    # Display the resulting frame
    cv2.imshow('Video', frame)

        


    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
video_capture.release()
cv2.destroyAllWindows()
