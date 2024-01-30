import easyocr

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

# Load the image with a real number plate (consider using a path to your image)
image_path = "C:\\Users\\HP\\Downloads\\SPAC\\hugging face\\assets\\number5.jpg"

# Perform text recognition
results = reader.readtext(image_path)

# Define the expected number plate lines
expected_number_plate_lines = ['MH 16 C', 'Z 7892']

# Convert the recognized lines to lowercase for case-insensitive matching
recognized_lines = [result[1].lower() for result in results]

# Check if each line of the expected number plate is present in the recognized text
found_all_lines = all(any(expected_line.lower() in recognized_line for recognized_line in recognized_lines) for expected_line in expected_number_plate_lines)

if found_all_lines:
    print("Welcome Authorized Person")
    print("The expected number plate is present in the image.")
else:
    print("Access Denied")
    print("Unauthorized person or the number plate is not recognized.")
