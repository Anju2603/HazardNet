import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the uploaded CSV
data = pd.read_csv("flood_data.csv")

# Select features and target
X = data[['Rainfall(mm)', 'Humidity(%)', 'Temp(degree C)', 'Elevation(m)']]
y = data['Risk']

# Encode target labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and label encoder
joblib.dump(model, 'flood_model.pkl')
joblib.dump(le, 'label_encoder.pkl')

# Evaluate accuracy
accuracy = model.score(X_test, y_test)
print(f"Model trained with accuracy: {accuracy * 100:.2f}%")
