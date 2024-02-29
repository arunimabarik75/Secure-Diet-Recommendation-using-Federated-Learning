# Secure Diet Recommendation using Federated Learning

This repository contains the implementation of a secure diet recommendation system using Federated Learning. The system predicts a healthy calorie intake for a user and suggests recipes based on the predicted calories.

## Overview

The system is divided into two main steps:

1. Predicting healthy calorie intake using Federated Learning.
2. Suggesting recipes based on the predicted calories using a Nearest Neighbor algorithm.

## Step 1: Predicting Healthy Calorie Intake

### User Input

The user provides their age, height, weight, gender, and activity level.

### Machine Learning Model Training

Follow these steps to train the model:

1. Clone the repository:
   ```bash
   git clone https://github.com/arunimabarik75/Secure-Diet-Recommendation-using-Federated-Learning.git
   ```
2. Navigate to the `Federated_Linear_Regression` directory:
   ```bash
   cd Federated_Linear_Regression
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:

   For Windows:
   ```bash
   venv\Scripts\activate
   ```
   For Linux:
   ```bash
   source venv/bin/activate
   ```
5. Install all dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Start the server:
   ```bash
   python server.py
   ```
7. Start the client (replace `1` with the number of each client):
   ```bash
   python client.py 1
   ```
   Each client should have a personal dataset to train on (e.g., `calories_train_1.csv`) and a common test dataset for all clients (e.g., `calories_test.csv`).

8. The global model parameters are saved in `global_model.sav`.

### Model Prediction

Use the model saved in `global_model.sav` to predict a healthy calorie intake.

### Output

The output is the predicted number of calories.

## Step 2: Suggest Recipes Based on Predicted Calories

### Dataset

The `recipes.csv` dataset is used for this step. It can be downloaded from [Kaggle](https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews?select=recipes.csv).

### Machine Learning

The Nearest Neighbor algorithm is used to suggest 15 recipes based on the predicted calories (5 recipes each for breakfast, lunch, and dinner). The full implementation can be found in the `Recommend_Diet_Nearest_Neighbors.ipynb` notebook.
