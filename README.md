Health Insurance Cost Prediction

This project aims to predict health insurance costs based on personal characteristics using machine learning algorithms. The dataset includes features such as age, gender, BMI, number of children, smoking status, and region. The goal is to build a predictive model to estimate the insurance charges for individuals.

Project Overview

Health insurance costs can vary significantly based on an individual’s profile. This project uses supervised learning techniques to develop models that can accurately predict these costs, helping insurance companies or individuals estimate expenses.

Dataset

The dataset used for this project includes the following features:

age: Age of the individual.
sex: Gender of the individual (male or female).
bmi: Body Mass Index, a measure of body fat based on height and weight.
children: Number of children/dependents covered by the insurance.
smoker: Whether the individual is a smoker (yes or no).
region: The region where the individual lives

Results

Best Model: The Random Forest Regressor performed the best, with an R² score of 0.85 and an MAE of $3,000.
Insights:

Smokers tend to have much higher insurance costs compared to non-smokers.
Age and BMI also significantly influence insurance charges.
Future Work
Improve model performance by hyperparameter tuning.
Test additional models like XGBoost.
Incorporate more advanced techniques like feature engineering.
Explore the possibility of using deep learning for predictions.
