# 🏥 Disease Prediction Using Machine Learning

A machine learning system that predicts a person's medical condition using their health and lifestyle data.

## 🎯 Aim
To build a model that accurately predicts medical conditions based on patient health data.

## 📊 Dataset
- Dataset: Disease Classification Dataset (Kaggle)
- Total Records: 30,000
- Features: 18 input features + 1 target (Medical Condition)

## 🔍 Key Insights
- Middle-aged adults carry the most risk with higher glucose and blood pressure
- Lifestyle habits strongly affect health outcomes
- High BMI often pairs with high glucose and worse medical conditions
- Aging and lifestyle choices drive most metabolic risk

## 🤖 Models Trained
- KNN, Naive Bayes, Decision Tree, Random Forest
- AdaBoost, Gradient Boosting, XGBoost, SVM
- **XGBoost achieved the best accuracy — 87%**

## 🛠️ Tech Stack
- Python, Scikit-learn, XGBoost
- SMOTE (for class balancing)
- Streamlit (web interface)
- Google Colab (model training)
- PyCharm (web app development)

## 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `streamlit run your_app/home.py`