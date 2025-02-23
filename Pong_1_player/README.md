Hand Tracking Game Using OpenCV and Mediapipe
📌 Overview
This is a simple hand-tracking game using OpenCV and Mediapipe, where you control a paddle with your hand to bounce a moving ball. The goal is to prevent the ball from falling off the screen while scoring points by hitting it with the virtual paddle.

🎮 How It Works
Uses a webcam to detect and track your hand.
The index finger acts as the paddle.
A ball moves randomly, bouncing off walls.
If the ball touches your paddle, you score a point.
If the ball falls off the screen, you lose a point.
The game ends when your score drops below zero.
🔧 Requirements

Ensure you have the following installed:
pip install opencv-python mediapipe

🚀 How to Run
Clone the repository:
git clone https://github.com/yourusername/Hand-Tracking-Game.git

Navigate to the project folder:
cd Hand-Tracking-Game

Run the script:
python hand_tracking_game.py
