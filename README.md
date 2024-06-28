# Wine-Quality-Prediction
This repository contains a machine learning project for predicting wine quality based on various physicochemical properties of the wine. The model is built using a Random Forest Classifier, and the application is deployed using Streamlit for an interactive user interface.

Features
* Predict wine quality (Good or Bad) based on user input of physicochemical properties.
* Utilizes a Random Forest Classifier trained on the wine quality dataset.
* Interactive web application built with Streamlit.

Installation
1 Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/wine-quality-prediction.git
cd wine-quality-prediction
2 Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3Install the required packages:

bash
Copy code
pip install -r requirements.txt
4 Run the Streamlit app:

bash
Copy code
streamlit run app.py

Usage
Open your browser and go to http://localhost:8501.
Use the sliders in the web app to input the physicochemical properties of the wine.
Click on the "Predict Quality" button to get the prediction (Good Wine or Bad Wine).

Dataset
The dataset used for training the model is the Wine Quality dataset available from the UCI Machine Learning Repository. The dataset contains various physicochemical properties of red wine and their quality ratings.

Files
*app.py: The Streamlit app for predicting wine quality.
* model.pkl: The trained Random Forest model.
* scaler.pkl: The scaler used for preprocessing the input features.
*requirements.txt: The list of required Python packages.
]
ontributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
* Create a new branch: git checkout -b feature-name.
* Make your changes and commit them: git commit -m 'Add some feature'.
* Push to the branch: git push origin feature-name.
* Create a pull request.


