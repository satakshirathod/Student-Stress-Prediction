from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import pickle
from datetime import datetime
import os

app = Flask(__name__)

# --- Database Configuration ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stress_history.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- Database Model ---
class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    anxiety = db.Column(db.Float)
    depression = db.Column(db.Float)
    sleep_quality = db.Column(db.Float)
    prediction_text = db.Column(db.String(200))
    category = db.Column(db.String(50))

# --- Create Database Automatically ---
with app.app_context():
    db.create_all()

# --- Load ML Model ---
try:
    with open("stress_model.pkl", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    print("Warning: stress_model.pkl not found or could not be loaded!")
    print(e)
    model = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return render_template(
            "index.html",
            prediction_text="Error: Model not loaded.",
            category="high"
        )

    try:
        # 1. Get all inputs from the form
        features = [float(x) for x in request.form.values()]

        # Safety check: model expects 8 inputs
        if len(features) != 8:
            return render_template(
                "index.html",
                prediction_text="Check HTML form. 8 inputs required.",
                category="high"
            )

        # 2. ML Model Prediction
        final_features = np.array([features])
        ml_prediction = int(model.predict(final_features)[0])

        # 3. Rule-Based Safety Net
        # Negative Factors - Higher is worse
        bad_factors = features[0] + features[1] + features[3] + features[6] + features[7]

        # Positive Factors - Higher is better
        good_factors = features[2] + features[4] + features[5]

        # Calculate Net Stress Score
        net_stress = bad_factors - good_factors

        # Hybrid Decision Logic
        if net_stress >= 20:
            prediction = 2
        elif net_stress <= 5:
            prediction = 0
        else:
            prediction = ml_prediction

        # 4. Result Text, Tips, and Gauge Value
        if prediction == 0:
            text = "Low Stress: You're doing great! Keep it up. 😊"
            category = "low"
            tips = [
                "Maintain your healthy sleep schedule.",
                "Keep up with your hobbies.",
                "Stay active."
            ]
            gauge_value = 20

        elif prediction == 1:
            text = "Medium Stress: You are experiencing moderate stress. 😐"
            category = "medium"
            tips = [
                "Take a 15-minute walk outside.",
                "Try 4-7-8 deep breathing.",
                "Listen to calming music."
            ]
            gauge_value = 50

        else:
            text = "High Stress: Please prioritize relaxation! 😟"
            category = "high"
            tips = [
                "Talk to a friend or family member.",
                "Disconnect from screens.",
                "Consider seeking professional support."
            ]
            gauge_value = 90

        # 5. Save to Database
      new_record = History(
    anxiety=features[0],
    depression=features[1],
    sleep_quality=features[2],
    prediction_text=text,
    category=category
)

        db.session.add(new_record)
        db.session.commit()

        return render_template(
            "index.html",
            prediction_text=text,
            category=category,
            tips=tips,
            gauge_value=gauge_value
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Server Error: {str(e)}",
            category="high"
        )

# --- Route to View History ---
@app.route("/history")
def view_history():
    records = History.query.order_by(History.date.desc()).all()
    return render_template("history.html", records=records)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)