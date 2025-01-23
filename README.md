
# Smart Plate Access Control System

This project is an automated access control system designed to ensure the security of a location by recognizing authorized vehicles through **number plate recognition** and **facial recognition**. The system uses **OpenCV**, **EasyOCR**, **Face Recognition**, **Streamlit**, and **Arduino** to automate the process. Once a vehicle’s number plate and driver's face are authorized, a **welcome sound** is played. If unauthorized, a **siren** is triggered to alert security.

## Features
- **Webcam Integration**: Captures images of vehicles and individuals for recognition.
- **Number Plate Recognition**: Uses **EasyOCR** to recognize and validate vehicle number plates.
- **Facial Recognition**: Uses **Face Recognition** library to authenticate the driver.
- **Siren Activation**: Activates a siren sound for unauthorized access.
- **Arduino Integration**: Sends signal to Arduino when an authorized person is detected.
- **Streamlit Interface**: A user-friendly interface for controlling and viewing the system.

## Requirements
To successfully run this project, the following dependencies are required:

1. **Python 3.x** (Preferably Python 3.7 or higher)
2. **Libraries**:
   - **streamlit**: `pip install streamlit`
   - **opencv-python**: `pip install opencv-python`
   - **pygame**: `pip install pygame`
   - **face_recognition**: `pip install face_recognition`
   - **easyocr**: `pip install easyocr`
   - **pyserial**: `pip install pyserial`
   
3. **Hardware Requirements**:
   - **Webcam** (for capturing images)
   - **Arduino Board** (for hardware control, like triggering siren)
   - **Relay module** (if using Arduino to control external devices like a siren)

## Project Setup

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/vinaypandey11/smart-plate-access-control.git
```

### Step 2: Install Required Libraries

After cloning the project, install all the required dependencies using pip:

```bash
cd smart-plate-access-control
pip install -r requirements.txt
```

Alternatively, you can manually install the dependencies:

```bash
pip install streamlit opencv-python pygame face_recognition easyocr pyserial
```

### Step 3: Configure the Arduino

1. Connect the **Arduino** board to your computer.
2. Ensure that the **COM port** is correctly identified (e.g., COM5). Modify the port in the code if necessary.

### Step 4: Prepare Media Files

Ensure the following files are available in the correct paths:
- **Welcome sound**: `welcome.mp3`
- **Siren sound**: `Siren.mpeg`
- **Reference facial image** for the person to be authorized (e.g., `vinay.jpg`).
  
**Note:** You can place these files in the directory of your project.

### Step 5: Run the Streamlit Application

1. Navigate to your project directory and run:

```bash
streamlit run app.py
```

2. The Streamlit web interface will open in your browser, and you will be able to interact with the system:
   - The webcam will start.
   - The **number plate** and **facial recognition** process will begin.
   - If **authorized**, a **welcome sound** is played, and a signal is sent to Arduino.
   - If **unauthorized**, a **siren sound** will play.

### Step 6: Access Control Logic

- **Number Plate Recognition**: The system scans the image and extracts the number plate. If it matches the predefined authorized plate (e.g., `MH16CZ7892`), it continues.
- **Facial Recognition**: The system compares the face in the captured image with the reference face (e.g., `vinay.jpg`). If matched, the user is authenticated.
- **Siren Control**: If unauthorized, the siren is triggered via **Arduino**, and a "Stop Siren" button is displayed to manually stop it from the Streamlit interface.

### Step 7: Interacting with the System

- **Capture Image**: Once the system starts, it will automatically capture an image using the webcam.
- **Recognition**: It will run the **number plate recognition** and **facial recognition** to validate if the user is authorized.
- **Access**: If both the number plate and face match the authorized criteria, the user gets access, and the system plays a welcome sound.
- **Siren**: If unauthorized, the system plays a siren, and you can stop it using the Streamlit button.

## Key Files & Functions
- **app.py**: Main Streamlit file for the web interface.
- **Siren.py**: Script to trigger the siren when unauthorized access is detected.
- **Face Recognition**: Matches the captured image’s face with the reference image.
- **EasyOCR**: Detects the number plate from the captured image.
- **Arduino Communication**: Sends a signal to Arduino to trigger external devices like a relay.

## Troubleshooting
1. **Webcam not working**: Ensure the camera is properly connected and check if it's being recognized by your system.
2. **Error in Serial Communication**: Ensure the correct **COM port** is specified and the Arduino is connected.
3. **Siren not stopping**: Click the **Stop Siren** button in the Streamlit interface to stop the sound. You can add an additional "Kill Switch" functionality on the Streamlit interface to manage siren stop.

## Snapshots
![a](https://github.com/user-attachments/assets/1995767c-66fe-477a-8f84-5e0fce50009f)
![b](https://github.com/user-attachments/assets/e6f08cc7-a806-40c7-ab52-2b28d52c801a)
![c](https://github.com/user-attachments/assets/d336042f-64ce-458e-b4f3-3ef1bfeddc21)
![d](https://github.com/user-attachments/assets/351f6d23-8b2f-45a7-a30a-839f18dbb72f)
![e](https://github.com/user-attachments/assets/98b04d01-849f-496b-9ce6-e63118cced70)
![f](https://github.com/user-attachments/assets/b969643e-e95c-4216-ae48-c76096797856)






