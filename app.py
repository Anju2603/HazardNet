from flask import Flask, render_template, request
import joblib
from weather_fetcher import get_weather_data

app = Flask(__name__)

# Load model and label encoder
model = joblib.load("flood_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

@app.route('/')
def home():
    return render_template('index.html', result=None)

@app.route('/predict', methods=['POST'])
def predict():
    city = request.form['city']
    features = get_weather_data(city)

    if features:
        prediction = model.predict([features])
        risk_label = label_encoder.inverse_transform(prediction)
        return render_template('index.html', result=f"🌧 Flood Risk in {city}: {risk_label[0]}")
    else:
        return render_template('index.html', result="❌ Could not fetch weather data. Try again.")

if __name__ == '_main_':
    app.run(debug=True)
