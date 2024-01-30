import cv2
import pytesseract
from pytesseract import Output
import re
# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Press 's' to save the frame and exit, or 'q' to exit without saving
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('captured_plate.jpg', frame)
        break
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()


# Read the captured image
image = cv2.imread('captured_plate.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply additional preprocessing like thresholding, blurring, etc.
# gray = cv2.threshold(gray, ...)

# Save or display the preprocessed image (optional)
cv2.imwrite('preprocessed_plate.jpg', gray)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imwrite('preprocessed_plate.jpg', thresh)

# Specify Tesseract path if it's not in the environment variables
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HP\tesseract.exe'

# Read the preprocessed image
preprocessed_image = cv2.imread('preprocessed_plate.jpg')

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(preprocessed_image, config='--psm 8 --oem 3')

# Print the text
print(text)


# Clean the OCR result
clean_text = re.sub('[^0-9]', '', text)

print(f"Cleaned License Plate Number: {clean_text}")
# import cv2
# import pytesseract
# import numpy as np

# # Function to preprocess the image
# # def preprocess_image(image):
# #     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# #     blur = cv2.GaussianBlur(gray, (5, 5), 0)
# #     thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# #     return thresh
# def preprocess_image(image):
#     # Convert to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Enhance contrast
#     alpha = 1.5
#     beta = 0
#     contrast_enhanced = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)

#     # Apply Gaussian blur
#     blur = cv2.GaussianBlur(contrast_enhanced, (5, 5), 0)

#     # Adaptive Thresholding
#     thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#     # Morphological operations
#     kernel = np.ones((1, 1), np.uint8)
#     img_dilation = cv2.dilate(thresh, kernel, iterations=1)
#     img_erosion = cv2.erode(img_dilation, kernel, iterations=1)

#     return img_erosion

# # Capturing the image from the webcam
# def capture_image():
#     cap = cv2.VideoCapture(0)

#     while True:
#         ret, frame = cap.read()
#         if ret:
#             cv2.imshow('Capture Image (Press "s" to save and exit)', frame)
#             if cv2.waitKey(1) & 0xFF == ord('s'):  # Press 's' key to save and exit
#                 cv2.imwrite('captured_image.jpg', frame)
#                 break

#     cap.release()
#     cv2.destroyAllWindows()


# # Main function
# def main():
#     # Capture an image from the webcam
#     capture_image()

#     # Read the captured image
#     image = cv2.imread('captured_image.jpg')

#     # Preprocess the image
#     preprocessed_image = preprocess_image(image)

#     # Use Tesseract to extract text
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HP\tesseract.exe'  # Update the path
#     text = pytesseract.image_to_string(preprocessed_image, config='--psm 8 --oem 3')

#     print("Recognized Text:", text)

# if __name__ == '__main__':
#     main()
