import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Food Waste AI Assistant",
    page_icon="🍽️",
    layout="wide"
)

MODEL_PATH = "model/demand_model.pkl"
DATA_PATH = "data/canteen_data.csv"

# --------------------------------------------------
# Load model and data
# --------------------------------------------------
try:
    model = joblib.load(MODEL_PATH)
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])
except FileNotFoundError:
    st.error(
        "Required files were not found. "
        "Please run generate_data.py and train_model.py first."
    )
    st.stop()

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("AI-Based Food Waste Prediction & Reduction Assistant")
st.subheader("Sustainable College Canteen Management")

st.write(
    "A machine-learning system that predicts meal demand "
    "and supports better food preparation decisions."
)

st.divider()

# --------------------------------------------------
# KPI cards
# --------------------------------------------------
total_prepared = int(df["meals_prepared"].sum())
total_consumed = int(df["meals_consumed"].sum())
total_leftover = int(df["leftover_meals"].sum())

waste_rate = (
    total_leftover / total_prepared * 100
    if total_prepared > 0 else 0
)

k1, k2, k3 = st.columns(3)

k1.metric("Total Meals Prepared", f"{total_prepared:,}")
k2.metric("Total Meals Consumed", f"{total_consumed:,}")
k3.metric("Total Leftovers", f"{total_leftover:,}")

st.caption(
    f"Historical sample-data leftover rate: {waste_rate:.1f}%"
)

st.divider()

# --------------------------------------------------
# Prediction section
# --------------------------------------------------
st.header("Today's Meal Demand Prediction")

col1, col2, col3 = st.columns(3)

with col1:
    students_expected = st.number_input(
        "Expected students",
        min_value=20,
        max_value=1000,
        value=200,
        step=10
    )

with col2:
    day_of_week = st.selectbox(
        "Day of week",
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
    )

with col3:
    menu_type = st.selectbox(
        "Menu type",
        [
            "Regular",
            "Special",
            "Breakfast",
            "Lunch"
        ]
    )

if st.button("Predict Meal Demand", type="primary"):

    input_data = pd.DataFrame({
        "day_of_week": [day_of_week],
        "menu_type": [menu_type],
        "students_expected": [students_expected]
    })

    prediction = model.predict(input_data)[0]

    predicted_meals = max(0, round(prediction))

    # Small buffer to reduce shortage risk
    recommended_preparation = round(predicted_meals * 1.03)

    # Buffer above prediction (not a real waste estimate)
    preparation_buffer = max(
        recommended_preparation - predicted_meals,
        0
    )

    # Persist results so the Sustainability Simulator can reuse them
    st.session_state["predicted_meals"] = predicted_meals
    st.session_state["recommended_preparation"] = recommended_preparation
    st.session_state["prediction_scenario"] = (
        f"{day_of_week} | {menu_type} | {students_expected} students"
    )

    # --------------------------------------------------
    # Prediction results
    # --------------------------------------------------
    st.success("Prediction completed successfully!")

    r1, r2, r3 = st.columns(3)

    r1.metric(
        "Predicted Demand",
        f"{predicted_meals} meals"
    )

    r2.metric(
        "Recommended Preparation",
        f"{recommended_preparation} meals"
    )

    r3.metric(
        "Preparation Buffer (3%)",
        f"+{preparation_buffer} meals"
    )

    # --------------------------------------------------
    # Explanation Assistant
    # --------------------------------------------------
    st.divider()

    st.header("Prediction Explanation Assistant")

    st.caption(
        "The notes below are illustrative guidance based on general "
        "patterns in the training data. They are not derived from "
        "the model's internal feature weights."
    )

    if menu_type == "Special":
        menu_explanation = (
            "The selected menu is Special, which can attract "
            "higher demand in the sample data."
        )
    elif menu_type == "Breakfast":
        menu_explanation = (
            "Breakfast entries in the sample data generally "
            "have lower demand than regular meal entries."
        )
    elif menu_type == "Lunch":
        menu_explanation = (
            "The selected menu is Lunch, so the prediction "
            "is based on historical lunch patterns."
        )
    else:
        menu_explanation = (
            "The selected menu is Regular, so the prediction "
            "uses historical regular-meal patterns."
        )

    if students_expected >= 250:
        student_explanation = (
            "The expected student count is relatively high, "
            "which increases the predicted demand."
        )
    elif students_expected <= 100:
        student_explanation = (
            "The expected student count is relatively low, "
            "which lowers the predicted demand."
        )
    else:
        student_explanation = (
            "The expected student count is within a normal "
            "range for the sample data."
        )

    st.info(
        f"Based on the selected conditions, the model predicts "
        f"approximately {predicted_meals} meals. "
        f"{student_explanation} {menu_explanation}"
    )

    # --------------------------------------------------
    # Recommendation
    # --------------------------------------------------
    st.subheader("Food Waste Reduction Recommendation")

    if preparation_buffer <= 5:
        st.success(
            "The recommended preparation amount is closely "
            "aligned with predicted demand."
        )
    else:
        st.warning(
            f"The recommended preparation includes a buffer of "
            f"{preparation_buffer} meals above predicted demand. "
            f"Consider preparing closer to predicted demand and "
            f"producing additional food in smaller batches if needed."
        )

# --------------------------------------------------
# Historical data
# --------------------------------------------------
st.divider()

st.header("Historical Canteen Data")

st.dataframe(
    df.sort_values("date").tail(20),
    use_container_width=True
)

# --------------------------------------------------
# Sustainability Impact Simulator
# --------------------------------------------------
st.divider()

st.header("Sustainability Impact Simulator")

st.write(
    "Estimate the potential reduction in unnecessary food preparation "
    "by comparing the current preparation plan with the AI recommendation."
)

planned_preparation = st.number_input(
    "Current planned meal preparation",
    min_value=20,
    max_value=2000,
    value=220,
    step=10
)

if st.button("Calculate Potential Impact"):

    # Reuse the saved prediction if the Predict button was already clicked;
    # otherwise run a fresh prediction from the current input values.
    if "recommended_preparation" in st.session_state:
        impact_recommended_meals = st.session_state["recommended_preparation"]
        impact_predicted_meals = st.session_state["predicted_meals"]
        scenario_label = st.session_state["prediction_scenario"]
        st.caption(f"Using saved prediction: {scenario_label}")
    else:
        impact_input = pd.DataFrame({
            "day_of_week": [day_of_week],
            "menu_type": [menu_type],
            "students_expected": [students_expected]
        })
        impact_prediction = model.predict(impact_input)[0]
        impact_predicted_meals = max(0, round(impact_prediction))
        impact_recommended_meals = round(impact_predicted_meals * 1.03)
        st.caption(
            "No saved prediction found. Run 'Predict Meal Demand' first "
            "for a consistent comparison. Showing a fresh estimate below."
        )

    potential_excess = max(
        planned_preparation - impact_recommended_meals,
        0
    )

    if planned_preparation > 0:
        potential_reduction = (
            potential_excess / planned_preparation
        ) * 100
    else:
        potential_reduction = 0

    # --------------------------------------------------
    # Impact metrics
    # --------------------------------------------------
    i1, i2, i3 = st.columns(3)

    i1.metric(
        "Current Preparation",
        f"{planned_preparation} meals"
    )

    i2.metric(
        "AI Recommendation",
        f"{impact_recommended_meals} meals"
    )

    i3.metric(
        "Potential Excess",
        f"{potential_excess} meals"
    )

    st.metric(
        "Potential Reduction",
        f"{potential_reduction:.1f}%"
    )

    # --------------------------------------------------
    # Impact explanation
    # --------------------------------------------------
    if potential_excess > 0:

        st.success(
            f"The AI recommendation could potentially avoid "
            f"preparing {potential_excess} unnecessary meals "
            f"under this scenario."
        )

        st.info(
            f"If the same pattern occurred 20 operating days per month, "
            f"the illustrative potential reduction would be approximately "
            f"{potential_excess * 20:,} meals per month."
        )

        st.caption(
            "This is an illustrative estimate based on the selected "
            "scenario and simulated project data. It is not a measured "
            "real-world reduction."
        )

    else:

        st.success(
            "The current preparation plan is already close to or below "
            "the AI recommendation."
        )

# --------------------------------------------------
# Food waste trend
# --------------------------------------------------
st.divider()

st.header("Food Waste Trend")

daily_waste = (
    df.groupby("date")["leftover_meals"]
    .sum()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(12, 4))

ax.plot(
    daily_waste["date"],
    daily_waste["leftover_meals"]
)

ax.set_xlabel("Date")
ax.set_ylabel("Leftover Meals")
ax.set_title("Daily Leftover Meal Trend")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

# --------------------------------------------------
# SDG alignment
# --------------------------------------------------
st.divider()

st.header("SDG Alignment")

st.write(
    "SDG 12 - Responsible Consumption and Production"
)

st.write(
    "The project supports responsible consumption by using "
    "AI-based demand prediction to help reduce unnecessary "
    "food preparation and potential food waste."
)

# --------------------------------------------------
# Responsible AI
# --------------------------------------------------
st.header("Responsible AI Considerations")

st.write(
    """
    - Transparency: predictions are based on defined input features
      such as expected students, day, and menu type.

    - Privacy: the prototype does not use personally identifiable
      student information.

    - Fairness: model performance should be evaluated with broader
      and more representative real-world canteen data.

    - Limitations: the current prototype uses simulated sample data,
      so predictions should not be treated as real operational
      recommendations without validation.
    """
)

# --------------------------------------------------
# Project information
# --------------------------------------------------
st.divider()

st.header("Project Information")

st.write(
    """
    Project: AI-Based Food Waste Prediction and Reduction Assistant

    Primary SDG: SDG 12 - Responsible Consumption and Production

    AI Technique: Machine-learning based demand prediction

    Target Users: College canteen staff and administrators

    Data: Simulated sample data for prototype demonstration
    """
)