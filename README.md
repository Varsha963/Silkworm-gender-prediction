# silkworm-gender-prediction
This project is a web-based AI tool that predicts silkworm gender using cocoon size, weight, texture, and color intensity. It uses a Random Forest model trained on sample data, provides predictions through a Flask web interface, and displays feature importance and accuracy for easy analysis.
Key Features:
ML Model with Random Forest:
Uses physical features: COCOON SIZE, WEIGHT, TEXTURE, COLOR INTENSITY.
Generates target labels (gender: Male/Female) automatically using a rule-based threshold.
Trains a Random Forest Classifier to predict silkworm gender.
Evaluates performance with accuracy score and confusion matrix.
Visualizes feature importance to show which attributes influence predictions the most.
Web Interface (Flask + HTML/JS):
Provides a simple, user-friendly form to input silkworm features.
Sends input data to the Flask backend via JSON.
Returns predicted gender as Male or Female.

Persistence:
Trained ML model is saved as vibrasense_model.pkl using pickle, enabling reuse without retraining.

Visualizations:
Confusion matrix and feature importance plots help analyze model behavior.
