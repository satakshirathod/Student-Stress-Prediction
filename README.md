# Student Stress Prediction System

A Flask-based Machine Learning web application that predicts a student's stress level based on academic, psychological, and social factors. The system takes multiple input parameters such as anxiety, depression, sleep quality, study load, academics, social support, peer pressure, and bullying, then predicts whether the student has low, medium, or high stress.

## Project Overview

The Student Stress Prediction System is designed to help analyze student stress levels using a trained machine learning model. The application provides a simple and interactive web interface where users can adjust input values and get an instant stress level prediction.

The project also stores prediction history using SQLite so that previous predictions can be viewed later.

## Features

- Student stress level prediction
- Machine learning model integration
- Flask-based backend
- Interactive user interface
- Input sliders for stress-related factors
- Low, medium, and high stress classification
- Stress management tips based on prediction
- Prediction history storage
- SQLite database integration
- Light/Dark theme option
- Responsive and clean UI

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- NumPy
- Scikit-learn
- SQLite
- HTML
- CSS
- JavaScript
- Pickle

## Project Structure

```text
Student-Stress-Prediction/
│
├── app.py
├── stress_model.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── history.html
│
├── instance/
│   └── stress_history.db
│
└── stress-report-final.pdf

Input Parameters

The model uses the following input parameters:

Anxiety
Depression
Sleep Quality
Study Load
Academics
Social Support
Peer Pressure
Bullying

Each input is taken through a slider-based interface.

Stress Categories

The application predicts stress into three categories:

Low Stress
Medium Stress
High Stress

Based on the prediction, the system also displays useful stress management tips.

How to Run the Project Locally
1. Clone the Repository
git clone https://github.com/your-username/Student-Stress-Prediction.git
2. Navigate to the Project Folder
cd Student-Stress-Prediction
3. Create Virtual Environment
python3 -m venv venv
4. Activate Virtual Environment

For macOS/Linux:

source venv/bin/activate

For Windows:

venv\Scripts\activate
5. Install Required Packages
pip install -r requirements.txt

If requirements file is not available, install manually:

pip install Flask Flask-SQLAlchemy numpy scikit-learn pandas joblib
6. Run the Application
python3 app.py
7. Open in Browser

Open the following URL in your browser:

http://127.0.0.1:5000/
Machine Learning Model

The trained model is saved as:

stress_model.pkl

The model is loaded in the Flask application using Python's pickle module.

Database

The project uses SQLite database to store prediction history.

Database file:

stress_history.db

The database is automatically created when the application runs.

Screenshots

Add screenshots of the application here.

Example:

![Home Page](screenshots/home.png)
![Prediction Result](screenshots/result.png)
![History Page](screenshots/history.png)
Future Enhancements
Add user authentication
Improve model accuracy with a larger dataset
Add graphical stress analysis
Export prediction history as PDF
Add admin dashboard
Deploy the application online
Add personalized recommendations
Author

Satakshi Rathod

License

This project is created for academic and learning purposes.


## GitHub par paste karne ka tarika

1. GitHub repo open karo  
2. **Add file → Create new file**  
3. File name likho:

```text
README.md
Upar wala content paste karo
Niche Commit changes click karo.

