# AI-Based Food Waste Prediction and Reduction Assistant

An AI-powered prototype for sustainable college canteen management that
predicts meal demand and helps reduce unnecessary food preparation.

## Project Overview

College canteens often prepare food based on estimated demand. When actual
demand is lower than expected, excess food can remain unused and contribute
to food waste.

This project uses machine learning to estimate meal demand based on:

- Expected number of students
- Day of the week
- Menu type

The system then provides a recommended preparation quantity and an
illustrative sustainability impact estimate.

## Sustainable Development Goal

### SDG 12 - Responsible Consumption and Production

The project supports responsible consumption by helping canteen staff
make more data-informed food preparation decisions.

## Key Features

- AI-based meal demand prediction
- Recommended meal preparation quantity
- Preparation buffer calculation
- Sustainability impact simulator
- Historical canteen data dashboard
- Food-waste trend visualization
- Responsible AI considerations
- IBM Bob-assisted code review and development

## AI / Machine Learning

### Model

Random Forest Regression

### Input Features

- Day of week
- Menu type
- Expected students

### Target

- Meals consumed

### Model Evaluation

The prototype currently uses simulated data.

- MAE: 8.58 meals
- RMSE: 10.81 meals
- R²: 0.9624
- Mean Bias: +0.76 meals
- Baseline MAE: 45.96 meals

> **Important:** These results are based on simulated prototype data.
> They should not be interpreted as real-world operational performance.

## Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest Regression
- Streamlit
- Matplotlib
- Joblib
- IBM Bob

## System Workflow

```text
Historical / Simulated Data
          ↓
Data Preparation
          ↓
Feature Selection
          ↓
Random Forest Model
          ↓
Meal Demand Prediction
          ↓
Preparation Recommendation
          ↓
Impact Simulation
          ↓
Sustainability Insights
