# Secure Diet Recommendation using Federated Learning

This repository contains implementation of a Diet Recommendation system using Federated Learning.

## Step - 1: Predicting healthy calorie intake 

### User Input
Age, Height, Weight, Gender and Activity Level

### Machine Learning 
#### Model Training
1. Clone the repository
   ```
   git clone https://github.com/arunimabarik75/Secure-Diet-Recommendation-using-Federated-Learning.git
   ```

2. Open Federated_Linear_Regression directory
   ```
   cd Federated_Linear_Regression
   ```

3. Create a virtual environment
   ```
   python -m venv venv
   ```
   
4. Enter virtual environment

   Windows ``` venv\Scripts\activate ```

   Linux ``` source venv/bin/activate ```

6. Install all dependencies
   ```
   pip install -r requirements.txt
   ```

7. Start server
   ```
   python server.py
   ```

8. Start client
   ```
   python client.py 1
   ```
   Replace 1 with the number of each client.

   Each client should have a personal dataset to train on (here calories_train_1.csv ...) and a common test dataset for all clients (here calories_test.csv).

10. Global model parameters saved in global_model.sav

#### Model Prediction
Use the model saved in global_model.sav to predict healthy calorie intake.

### Output
Calories

## Step - 2: Suggest recipes based on predicted calories
### Dataset
recipes.csv - https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews?select=recipes.csv

### Machine Learning
Nearest Neighbor algorithm suggests 15 recipes based on the calories predicted (5 recipes each for breakfast, lunch and dinner)

Full implementation - Recommend_Diet_Nearest_Neighbors.ipynb 
