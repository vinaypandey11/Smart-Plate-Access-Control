# import easyocr

# # Initialize the EasyOCR reader
# reader = easyocr.Reader(['en'])

# # Load the image
# image = "C:\\Users\\HP\\Downloads\\SPAC\\hugging face\\assets\\number.jpg"
# #image = "C:\\Users\\HP\\Downloads\\SPAC\\hugging face\\assets\\number1.jpg"

# # Perform text recognition
# results = reader.readtext(image)

# # Check if the number is present in the extracted text
# found_number = any('MH 16 CZ 7892' in result[1] for result in results)

# if found_number:
#     print("Welcome Authorised Person")
#     print("The text is present in the image.")
   
# else:
#     print("Access Denied")
#     print("Unauthorised person")
#     print("The text is not present in the image.")


# import cv2
# import easyocr

# def capture_image_from_webcam():
#     cap = cv2.VideoCapture(0)
#     print("Press 'c' to capture the image.")

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to grab frame")
#             break

#         cv2.imshow('Webcam Live', frame)

#         if cv2.waitKey(1) & 0xFF == ord('c'):
#             cv2.imwrite('captured_image.jpg', frame)
#             print("Image captured.")
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     return 'captured_image.jpg'

# # Initialize the EasyOCR reader
# reader = easyocr.Reader(['en'])

# # Capture image from webcam
# image_path = capture_image_from_webcam()

# # Perform text recognition
# results = reader.readtext(image_path)
# print(results)
# # Check if the number is present in the extracted text
# found_number = any('MH 16 BN 5447' in result[1] for result in results)

# if found_number:
#     print("Welcome Authorised Person")
#     print("The text is present in the image.")
# else:
#     print("Access Denied")
#     print("Unauthorised person")
#     print("The text is not present in the image.")

# import cv2
# import easyocr

# def capture_image_from_webcam():
#     cap = cv2.VideoCapture(0)
#     print("Press 'c' to capture the image.")

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to grab frame")
#             break

#         cv2.imshow('Webcam Live', frame)

#         if cv2.waitKey(1) & 0xFF == ord('c'):
#             cv2.imwrite('captured_image.jpg', frame)
#             print("Image captured.")
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     return 'captured_image.jpg'

# # Initialize the EasyOCR reader
# reader = easyocr.Reader(['en'])

# # Capture image from webcam
# image_path = capture_image_from_webcam()

# # Perform text recognition
# results = reader.readtext(image_path)

# # Display recognized text in a proper number plate format
# recognized_text = ' '.join(result[1] for result in results)
# print(f"Recognized Text: {recognized_text}")

# # Check if the specific number plate format is present in the recognized text
# desired_number_plate = 'MH 16 DF 0608'
# found_number_plate = desired_number_plate in recognized_text

# if found_number_plate:
#     print("Welcome Authorised Person")
#     print("The expected number plate is present in the image.")
# else:
#     print("Access Denied")
#     print("Unauthorised person")
#     print("The expected number plate is not present in the image."
# )

import cv2
import easyocr

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

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

# Capture image from webcam
image_path = capture_image_from_webcam()

# Perform text recognition
results = reader.readtext(image_path)

# Extract only alphanumeric characters (letters and numbers) and combine them
recognized_text = ''.join(''.join(char for char in result[1] if char.isalnum()) for result in results)

print(f"Recognized Text: {recognized_text}")

# Define the specific number plate format (without spaces for comparison)
desired_number_plate = 'MH16DF0608'

# Check if the specific number plate format is present in the recognized text
found_number_plate = desired_number_plate in recognized_text

if found_number_plate:
    print("Welcome Authorised Person")
    print("The expected number plate is present in the image.")
else:
    print("Access Denied")
    print("Unauthorised person")
    print("The expected number plate is not present in the image.")
