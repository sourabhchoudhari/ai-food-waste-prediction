import pandas as pd
import numpy as np

np.random.seed(42)

rows = []

menu_types = ["Regular", "Special", "Breakfast", "Lunch"]

for i in range(300):
    date = pd.Timestamp("2025-01-01") + pd.Timedelta(days=i)

    day_of_week = date.day_name()

    if day_of_week == "Sunday":
        expected = np.random.randint(50, 100)
    elif day_of_week == "Saturday":
        expected = np.random.randint(100, 170)
    else:
        expected = np.random.randint(160, 280)

    menu_type = np.random.choice(menu_types)

    # Some menu types attract slightly different demand
    if menu_type == "Special":
        expected += np.random.randint(10, 35)
    elif menu_type == "Breakfast":
        expected -= np.random.randint(20, 50)

    expected = max(expected, 50)

    # Students who actually eat
    served = int(expected * np.random.uniform(0.82, 0.98))

    # Small variation between meals prepared and served
    prepared = int(served * np.random.uniform(1.02, 1.15))

    # Actual meals consumed
    consumed = int(served * np.random.uniform(0.94, 1.00))

    leftover = max(prepared - consumed, 0)

    rows.append([
        date.strftime("%Y-%m-%d"),
        day_of_week,
        menu_type,
        expected,
        served,
        prepared,
        consumed,
        leftover
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "date",
        "day_of_week",
        "menu_type",
        "students_expected",
        "students_served",
        "meals_prepared",
        "meals_consumed",
        "leftover_meals"
    ]
)

df.to_csv("data/canteen_data.csv", index=False)

print("Dataset created successfully!")
print(f"Total records: {len(df)}")
print(df.head())