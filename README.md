Hand Gesture Recognition using MediaPipe and OpenCV
📌 Overview
This project implements real-time hand gesture recognition using MediaPipe Hands and OpenCV. The system detects hand landmarks, calculates distances between keypoints, and classifies gestures based on pre-trained data.

🚀 Features
Real-time hand tracking using MediaPipe
Custom gesture training for user-defined gestures
Gesture classification based on keypoint distances
Live visualization with OpenCV
🛠️ Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/Hand-Gesture-Recognition.git
cd Hand-Gesture-Recognition
Install dependencies
Ensure you have Python 3 installed, then run:

bash
Copy
Edit
pip install opencv-python mediapipe numpy
Run the script

bash
Copy
Edit
python hand_gesture.py
🎯 Usage
Train gestures

Enter the number of gestures to recognize
Provide names for each gesture
Show the gesture and press 't' to record it
Recognize gestures

Once training is complete, the system detects and classifies gestures in real time
Press 'q' to exit
🖥️ Code Explanation
Hand Tracking: Uses MediaPipe to detect and track hand landmarks
Distance Calculation: Computes Euclidean distance between keypoints
Gesture Matching: Compares detected gesture with pre-trained gestures
OpenCV Visualization: Displays hand landmarks and recognized gesture
📌 Key Functions
Function	Description
Hands(frame)	Detects hands and returns key landmark positions
location(datapoints)	Computes distance matrix for landmarks
findError(knownmatrix, unknownmatrix, keypoints)	Calculates error between gestures
findGestour(knownAllGestures, unknownGesture, tol, gestNames, keypoints)	Matches gesture with trained gestures
📷 Demo
(Include sample images or GIFs of the working project)

🤝 Contributing
Feel free to fork and improve the project! Create a pull request if you have enhancements.

🛡️ License
This project is open-source and available under the MIT License.
