# AI-Based Food Waste Prediction and Reduction Assistant

An AI-powered prototype for sustainable college canteen management that predicts meal demand and supports better food preparation decisions.

## Problem Statement

College canteens often prepare food based on estimated student demand rather than data-driven predictions. When actual consumption is lower than expected, excess food may remain unused and contribute to food waste.

This project addresses this challenge by using machine learning to estimate meal demand based on expected students, day of the week, and menu type. The system then provides a recommended preparation quantity and an illustrative sustainability impact estimate. The aim is to support canteen staff in making more informed food preparation decisions and encourage responsible use of food resources.

## Proposed Solution

The project provides a Streamlit-based decision-support application for college canteens.

The system:

1. Uses simulated historical canteen data.
2. Trains a Random Forest Regression model.
3. Predicts expected meal consumption.
4. Provides a recommended preparation quantity with a preparation buffer.
5. Compares current planned preparation with the AI recommendation.
6. Provides an illustrative potential over-preparation reduction estimate.
7. Displays historical canteen data and food-waste trends.

## SDG Alignment

### SDG 12 - Responsible Consumption and Production

The project supports responsible consumption by helping canteen staff make more data-informed food preparation decisions and identify potential over-preparation.

## Key Features

- AI-based meal demand prediction
- Recommended meal preparation quantity
- Preparation buffer calculation
- Sustainability impact simulator
- Historical canteen data dashboard
- Food-waste trend visualization
- Responsible AI information
- IBM Bob-assisted development and code review

## AI / Machine Learning

### Model

**Random Forest Regression**

### Input Features

- Expected number of students
- Day of the week
- Menu type

### Target

- Meals consumed

### Prototype Evaluation

The current prototype uses **simulated data**.

- **MAE:** 8.58 meals
- **RMSE:** 10.81 meals
- **R²:** 0.9624
- **Mean Bias:** +0.76 meals
- **Baseline MAE:** 45.96 meals

> These metrics are based on simulated prototype data and should not be interpreted as real-world operational performance.

## Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest Regression
- Streamlit
- Matplotlib
- Joblib
- GitHub
- IBM Bob

## Project Workflow

```text
Simulated Historical Data
          ↓
Data Preparation
          ↓
Feature Selection
          ↓
Random Forest Training
          ↓
Meal Demand Prediction
          ↓
Preparation Recommendation
          ↓
Sustainability Impact Simulation
          ↓
Visualization and Insights

IBM Bob Integration
IBM Bob was incorporated into the project development workflow for:
- Code troubleshooting
- Structured code review
- Identifying bugs and structural issues
- Improving application reliability
- Reviewing and improving the machine-learning training workflow
- Applying targeted code changes
IBM Bob was used to review both the Streamlit application and the model training workflow while preserving the intended project functionality.
Project Structure
ai-food-waste-prediction/
│
├── app.py
├── train_model.py
├── generate_data.py
├── requirements.txt
├── README.md
│
├── data/
│   └── canteen_data.csv
│
├── model/
│   ├── demand_model.pkl
│   └── model_metadata.json
│
└── screenshots/

How to Run
1. Clone the repository
git clone https://github.com/sourabhchoudhari/ai-food-waste-prediction.git
cd ai-food-waste-prediction

2. Install dependencies
pip install -r requirements.txt

3. Generate the dataset
python generate_data.py

4. Train the model
python train_model.py

5. Run the Streamlit application
streamlit run app.py
 
Responsible AI and Limitations
Transparency
The application clearly identifies that the dataset and impact calculations are simulated. The displayed model metrics are therefore prototype evaluation results.
Privacy
The prototype does not use personally identifiable student information.
Fairness
The model should be evaluated using broader and more representative real-world canteen data before practical use.
Ethics
The system is intended as a decision-support tool and should not be treated as an automated authority for food preparation decisions.
Simulated Data Limitation
The current prototype uses simulated canteen data. The impact values shown by the application are illustrative estimates and should not be interpreted as measured real-world food-waste reductions.
Future Scope
Future versions could use real canteen data and additional factors such as:
- Weather conditions
- Holidays
- College events
- Historical menu popularity
- Seasonal patterns
The model could then be retrained and validated using real operational data.
