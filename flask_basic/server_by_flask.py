import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

with open(r"C:\Users\DELL\Downloads\spam_model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.json  # Get the JSON data from the request
    X_test_vec = vectorizer.transform(customer)
    prediction = model.predict(X_test_vec)
    return jsonify({'prediction': 'Spam' if prediction[0] == 1 else 'Not Spam'})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)