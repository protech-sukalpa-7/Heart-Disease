# ❤️ Heart Disease Prediction System

A modern **Machine Learning-powered Heart Disease Prediction System** built using **Flask**, **Scikit-learn**, and **Python**. The application predicts whether a patient is at **high** or **low risk** of heart disease based on clinical and demographic features using a **Stacking Ensemble Learning Model**.

The project combines data preprocessing, feature engineering, ensemble learning, and a responsive web interface to deliver accurate and real-time heart disease risk predictions.

---

# 🚀 Project Overview

Cardiovascular disease remains one of the leading causes of death worldwide. Early identification of high-risk patients can significantly improve treatment outcomes and preventive care.

This project leverages **Ensemble Machine Learning** by combining multiple predictive models into a **Stacking Classifier**, resulting in improved prediction accuracy compared to individual algorithms. Users can enter patient information through a web interface, and the system instantly predicts the likelihood of heart disease.

---

# ✨ Features

* ❤️ Predicts heart disease risk in real time
* 🤖 Stacking Ensemble Machine Learning model
* 📊 Displays prediction probability/confidence
* 🌐 Interactive Flask web application
* ⚡ Fast and lightweight prediction engine
* 🧹 Automated preprocessing pipeline
* 🔢 Feature scaling using StandardScaler
* 🏷️ Categorical feature encoding
* 🎨 Clean and responsive user interface
* 📱 Easy-to-use patient input form

---

# 🩺 Input Features

The prediction model utilizes several clinical and demographic parameters, including:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol Level
* Fasting Blood Sugar
* Resting ECG Results
* Maximum Heart Rate Achieved
* Exercise-Induced Angina
* ST Depression (Oldpeak)
* Slope of Peak Exercise ST Segment
* Number of Major Vessels (CA)
* Thalassemia
* Dataset Source

---

# 🛠️ Technology Stack

## Programming Language

* Python

## Backend

* Flask

## Machine Learning

* Scikit-learn
* Stacking Ensemble Learning
* StandardScaler
* Label Encoding

## Data Processing

* Pandas
* NumPy
* Joblib

---

# ⚙️ Machine Learning Pipeline

1. Load the trained stacking model.
2. Load saved encoders and scaler.
3. Accept patient information through the web interface.
4. Encode categorical features.
5. Scale numerical features.
6. Generate heart disease prediction.
7. Display risk level and prediction probability.

---

# 📁 Project Structure

```text
Heart-Disease-Prediction/
│
├── app.py
├── heart_disease_stacking_model.pkl
├── scaler.pkl
├── encoder.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/protech-sukalpa-7/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

Then open your browser and navigate to:

```text
http://127.0.0.1:5000
```

---

# 📈 Model Information

| Component            | Description                           |
| -------------------- | ------------------------------------- |
| Problem Type         | Binary Classification                 |
| Model                | Stacking Ensemble Classifier          |
| Feature Scaling      | StandardScaler                        |
| Categorical Encoding | Label Encoding                        |
| Backend              | Flask                                 |
| Input                | Patient Clinical Data                 |
| Output               | High Risk / Low Risk of Heart Disease |

---

# 🎯 Future Improvements

* Explainable AI using SHAP
* Model comparison dashboard
* REST API integration
* Patient history management
* Doctor login and authentication
* Cloud deployment
* Electronic Health Record (EHR) integration
* Deep Learning model comparison

---

# 📷 Screenshots

Include screenshots of:

* 🏠 Home Page
* 📝 Patient Information Form
* 📊 Prediction Result
* 📈 Risk Probability Output

---

# 👨‍💻 Author

## Sukalpa Manna

**AI | Machine Learning | Data Science Developer**

GitHub: https://github.com/protech-sukalpa-7

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 🙏 Acknowledgements

* Scikit-learn
* Flask
* Pandas
* NumPy
* Python Community
* Open Source Machine Learning Community
