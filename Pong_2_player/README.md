🏓 Hand Tracking Pong Game Using OpenCV & Mediapipe
🚀 A fun hand-tracking Pong game where you control the paddles using your hands instead of a keyboard or mouse! 🎮

📌 Overview
This project uses OpenCV and Mediapipe to track your hands in real-time and control the left and right paddles in a pong-style game. The game keeps track of individual scores for left and right hands, and players must keep the ball bouncing to earn points.

🎯 Features
✅ Real-time hand tracking using Mediapipe
✅ Left and right hand detection for two-player control
✅ Dynamic ball movement with changing direction on paddle hit
✅ Score tracking for both hands
✅ Smooth game interaction using OpenCV

🖥️ How It Works?
1️⃣ The index finger of each hand acts as a paddle.
2️⃣ The ball moves across the screen, bouncing off walls.
3️⃣ The goal is to block the ball from passing your side.
4️⃣ If the ball hits your paddle, you gain a point. If it passes your side, you lose a point.
5️⃣ The game continues until you decide to quit (Press 'Q').

⚙️ Installation & Setup
Step 1: Clone the Repository

git clone https://github.com/subu8098/Medium_AI_projects.git
cd Medium_AI_projects

Step 2: Install Dependencies

pip install opencv-python mediapipe
Step 3: Run the Game
bash
Copy
Edit
python hand_tracking_pong.py
📌 Note: Make sure your webcam is connected before running the script.


🛠 Technologies Used
🔹 Python – Main programming language
🔹 OpenCV – For real-time video processing
🔹 Mediapipe – For hand tracking

