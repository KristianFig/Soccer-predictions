
<img width="1265" alt="Screenshot 2024-07-08 at 4 10 22 PM" src="https://github.com/KristianFig/Soccer-predictions/assets/167266044/cb49660f-43cd-48b9-9683-23052166b763">

# Project Overview: Predicting Copa America

## Project Motivation
As a soccer enthusiast and with the Copa America tournament being hosted in the USA, I embarked on this project to predict match outcomes for the tournament. The project combines my passion for soccer with the practical application of data science techniques, making it both enjoyable and timely.

## Data Source
The dataset used for this project is "International football results from 1872 to 2024," downloaded from Kaggle. This dataset includes comprehensive historical match data, providing all the necessary information for analysis and model building.

## Tools and Technologies
- **Jupyter Notebook:** For initial data exploration, cleaning, and feature engineering.
- **PyCharm:** For developing and testing the prediction model and server-side code.
- **Postman:** For testing API endpoints.
- **Visual Studio Code:** For creating the front-end of the web application.

## Methodology

### 1. Data Cleaning and Feature Engineering
- Performed data cleaning to handle missing values and inconsistencies.
- Engineered relevant features such as team averages and match outcomes.
- Visualized data using histograms and scatter plots.
- Removed outliers to improve model performance.

### 2. Feature Selection
- Applied Recursive Feature Elimination (RFE) and feature importance using Random Forest to identify significant features.

### 3. Model Testing and Evaluation
- Tested multiple models including Logistic Regression, Decision Tree, and Random Forest.
- Evaluated models using metrics such as Hamming Loss, Subset Accuracy, Precision, Recall, and F1-score.
- Selected the best-performing model and exported it as a pickle file for deployment.

### 4. Deployment
- Developed utility and server scripts in PyCharm to create API endpoints.
- Tested endpoints in Postman to ensure correct functionality.
- Created a web application in Visual Studio Code with pages for home, predict_winner, project overview, and resume.
