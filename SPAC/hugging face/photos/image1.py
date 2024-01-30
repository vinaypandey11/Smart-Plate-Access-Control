import cv2
import easyocr

def capture_image_from_webcam():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Display the resulting frame
        cv2.imshow('Webcam Live', frame)

        # Wait for the 'c' key to be pressed to capture the image
        if cv2.waitKey(1) & 0xFF == ord('c'):
            print("Capturing image...")
            # Save the captured image
            cv2.imwrite('captured_image.jpg', frame)
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    return 'captured_image.jpg'

def read_number_plate(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Create an EasyOCR reader instance
    reader = easyocr.Reader(['en'])

    # Detect text from the image
    results = reader.readtext(image)

    # Extract and print recognized numbers
    recognized_numbers = []
    for (bbox, text, prob) in results:
        recognized_numbers.append(text)

    # Print the recognized numbers
    print("Recognized Numbers:", recognized_numbers)
    desired_numbers={'MH 16 DF 0608'}
    if check_matching_numbers(recognized_numbers, desired_numbers):
        print("Authorized")
    else:
        print("Unauthorized")

def check_matching_numbers(recognized_numbers, desired_numbers):
    # Check if any recognized number matches with desired numbers
    for number in recognized_numbers:
        if number in desired_numbers:
            return True
    return False
    

# Capture image from webcam
image_path = capture_image_from_webcam()

# Read number plate from the captured image and display recognized numbers
read_number_plate(image_path)

