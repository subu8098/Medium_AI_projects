Spam Detection API using Flask
This repository contains a Flask-based API for detecting spam messages using a pre-trained machine learning model. The model utilizes TF-IDF vectorization and predicts whether an input message is Spam or Not Spam.

🚀 Features
Load a pre-trained Spam Detection Model (spam_model.pkl).
Process input text using TF-IDF Vectorization.
Serve predictions via a Flask API.
Accept text input through a POST request (/predict).
Simple client script to test the API.
📌 Installation
1️⃣ Clone the repository

sh
Copy
Edit
git clone https://github.com/subu8098/Medium_AI_projects.git
cd Medium_AI_projects/spam-detection-api
2️⃣ Create a virtual environment (optional but recommended)

sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
3️⃣ Install dependencies

sh
Copy
Edit
pip install -r requirements.txt
🛠️ Usage
1️⃣ Run the Flask Server
sh
Copy
Edit
python app.py
The server will start on http://localhost:9696.
2️⃣ Send a Prediction Request
Run the following Python script:

python
Copy
Edit
import requests

customer = ["Congratulations! You won a free iPhone!"]
url = 'http://localhost:9696/predict'
response = requests.post(url, json=customer)
result = response.json()
print(result)  # {'prediction': 'Spam' or 'Not Spam'}
📂 Project Structure
bash
Copy
Edit
📦 spam-detection-api
│── app.py                  # Flask server
│── requirements.txt        # Dependencies
│── spam_model.pkl          # Pre-trained model
│── client.py               # Sample client script
│── README.md               # Project documentation
📌 API Endpoint
Method	Endpoint	Description
POST	/predict	Predicts Spam or Not Spam
Request Format:
json
Copy
Edit
["Your message here"]
Response Format:
json
Copy
Edit
{"prediction": "Spam" or "Not Spam"}
📖 Dependencies
Flask
Scikit-learn
Pickle
Requests
Install all dependencies using:

sh
Copy
Edit
pip install -r requirements.txt
💡 Future Improvements
Deploy API using Docker or Cloud Platforms.
Improve model accuracy using Deep Learning techniques.
Extend API to support batch predictions.
📬 Contributing
Feel free to contribute! Open an issue or submit a pull request if you have improvements.

📜 License
This project is open-source and available under the MIT License.
