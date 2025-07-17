import joblib
from weather_fetcher import get_weather_data

# Load model and encoder
model = joblib.load("flood_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Get real-time weather for a city
city = "Gurgaon"  # You can change this
features = get_weather_data(city)

if features:
    prediction = model.predict([features])
    risk_label = label_encoder.inverse_transform(prediction)
    print(f"🌧 Predicted flood risk in {city}: {risk_label[0]}")
else:
    print("Failed to fetch weather data.")
