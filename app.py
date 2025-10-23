from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

# Correct: Flask app should be initialized with __name__
app = Flask(__name__)

# Load your trained ML model
model = pickle.load(open("vibrasense_model.pkl", "rb"))

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from request
    data = request.get_json()
    # Convert input features to numpy array and reshape
    features = np.array(data['features']).reshape(1, -1)
    # Make prediction
    prediction = model.predict(features)[0]
    # Return result as JSON
    return jsonify({'result': int(prediction)})

# Correct the Flask entry point
if __name__ == '__main__':
    app.run(debug=True)
