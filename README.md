# Insurance Cost Prediction

## Overview
This is a machine learning project that predicts insurance costs based on various features such as age, sex, BMI, number of children, smoker status, and region.

## Dataset
The dataset used for training and testing the model is stored in the 'insurance.csv' file. It contains 1338 entries and 7 columns, including age, sex, BMI, children, smoker, region, and charges.

## Data Preprocessing
The data is preprocessed to handle missing values and convert categorical variables into numerical format. The 'sex' column is mapped to 0 for female and 1 for male, and the 'smoker' column is mapped to 0 for 'no' and 1 for 'yes'. The 'region' column is mapped to numerical codes (1 to 4) for the respective regions.

## Model Training
Four regression models are trained using the scikit-learn library:
- Linear Regression
- Support Vector Regressor (SVR)
- Random Forest Regressor
- Gradient Boosting Regressor

## Model Evaluation
The performance of each model is evaluated using the R-squared (R2) metric and the mean absolute error (MAE) on the test data.

## Predicting Insurance Cost for New Customers
A GUI (Graphical User Interface) is provided to enter the details of a new customer, such as age, sex, BMI, children, smoker status, and region. The trained Gradient Boosting Regressor model is used to predict the insurance cost for the new customer.

## Getting Started
To run the prediction GUI locally, follow these steps:

1. Install the required dependencies:
   ```bash
   pip install pandas scikit-learn joblib tkinter
Clone this repository and navigate to the project directory.

Run the GUI script:

bash
Copy code
python insurance_cost_prediction_gui.py
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Special thanks to the scikit-learn team for providing the machine learning library.

Feel free to use and modify this code for your own projects!

vbnet
Copy code

Replace `insurance_cost_prediction_gui.py` with the actual filename of your GUI script if it's different.

Remember to include the relevant details about your project, such as any addition
