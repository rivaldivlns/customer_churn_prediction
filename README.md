# Customer Churn Prediction

Welcome to the Customer Churn Prediction project! This project aims to predict the likelihood of customer churn using machine learning models. Understanding and predicting customer churn is crucial for businesses to maintain sustainability and growth. The project is organized with the following folder structure:

## Background

In the dynamic business landscape, retaining customers is paramount for sustained success. Customer churn, the phenomenon where customers discontinue using a product or service, poses a significant challenge for many companies. Addressing this challenge, the Customer Churn Prediction project is designed to assist businesses in identifying potential churners. Leveraging machine learning techniques, the project aims to create a predictive model capable of estimating the likelihood of churn for each customer based on historical data.

Through exploratory data analysis (EDA) and well-documented model development in the Jupyter notebook (`customer_churn.ipynb`), the project provides insights into the factors that may contribute to customer decisions to discontinue subscriptions or services.

Additionally, the deployment folder (`deployment`) contains files essential for the application's deployment, including `app.py` for interactive churn prediction, `eda.py` for exploratory data analysis, `model.pkl` for the pre-trained machine learning model, `prediction.py` for prediction functionality, and `requirements.txt` listing necessary dependencies.

## Folder Structure

1. **Deployment:** This folder contains files related to the application deployment.
    - `app.py`: This file is part of the web application for churn prediction.
    - `eda.py`: This file contains exploratory data analysis for initial dataset understanding.
    - `model.pkl`: This file holds the pre-trained machine learning model ready for use.
    - `prediction.py`: This file is responsible for making churn predictions using the deployed model.
    - `requirements.txt`: This file includes a list of required dependencies. Use `pip install -r requirements.txt` to install them.

2. **Notebooks:** This folder contains Jupyter notebooks dedicated to development and analysis.
    - `customer_churn.ipynb`: This notebook functions as a development workspace, providing steps for both model development and data analysis.

3. **Data:** This section contains the raw data used in the project.
    - `data.csv`: This file comprises the customer dataset utilized for training and testing the predictive model.

## How to Use

1. **Exploratory Data Analysis (EDA):** If you want to gain a deeper understanding of the dataset, run `eda.py`. This script provides valuable exploratory data analysis.

2. **Model Development:** To view the step-by-step model development process, open and run the Jupyter notebook `customer_churn.ipynb`.

3. **Application Deployment:** To use the web application for churn prediction, run `app.py`. Ensure all dependencies are installed by running `pip install -r deployment/requirements.txt`.

## Contribution

Contributions to this project are welcome! Feel free to create a new branch, make changes, and submit a pull request.

## Contact

If you have any questions or issues, please contact me at [rivaldivalensia5@gmail.com].
