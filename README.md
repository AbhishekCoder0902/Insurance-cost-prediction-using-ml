# Insurance Cost Prediction

This is a simple Python application that uses Tkinter for GUI and GradientBoostingRegressor for insurance cost prediction. The application allows users to input various factors related to the customer, such as age, sex, BMI, number of children, smoking status, and region, and then predicts the insurance cost for the customer using a pre-trained machine learning model.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- Pandas
- Scikit-learn
- Tkinter (included in Python standard library)
- Joblib

You can install the required packages using pip:

pip install pandas scikit-learn joblib


## Usage

1. Clone the repository to your local machine.

2. Make sure you have the `model_joblib_gr` file in the same directory as the `app.py` script. This file contains the pre-trained GradientBoostingRegressor model.

3. Run the application by executing the `app.py` script:


4. The GUI window will open, prompting you to enter various details related to the customer.

5. Input the customer's age, sex (0 for female, 1 for male), BMI, number of children, smoking status (0 for no, 1 for yes), and region (1 to 4).

6. Click the "Predict" button to see the predicted insurance cost for the customer.

Please note that the input values should be provided in the correct format. If any invalid input is given, an error message will be displayed.

## Model Details

The insurance cost prediction model is based on the GradientBoostingRegressor algorithm from the scikit-learn library. It has been trained on a dataset containing information about various customers and their corresponding insurance costs. The model uses this information to make predictions for new customers based on their characteristics.

## Disclaimer

This application is intended for educational and demonstration purposes only. The insurance cost predictions made by the model may not reflect actual insurance costs and should not be used for real-world decision-making. The accuracy of the predictions depends on the quality and size of the training data and the performance of the machine learning model.

## Credits

- The application is created by Priyadarshi Abhishek.
- The machine learning model used in the application is trained on publicly available insurance data.

Feel free to modify, improve, and use this application as you see fit. If you encounter any issues or have suggestions for improvement, please feel free to raise an issue or submit a pull request. Enjoy predicting insurance costs with the application!


