"""
Advanced Tutorial: Conditional Statements (if / elif / else) in Data Analysis
-----------------------------------------------------------------------------
In data analysis, conditional statements are critical for:
    - Cleaning and validating data
    - Categorizing continuous values
    - Creating derived features
    - Controlling data pipelines

Key Concepts:
    - Classic conditional blocks
    - Inline conditional expressions
    - Vectorized conditions in pandas
    - Using conditions inside list comprehensions
"""

import numpy as np
import pandas as pd

# -------------------------------------------
# 1. Basic Conditional Statements
# -------------------------------------------
print("1) Basic Conditional Statements")

VALUE = 85

if VALUE >= 90:
    GRADE = "A"
elif VALUE >= 80:
    GRADE = "B"
else:
    GRADE = "C"

print(f"Score: {VALUE}, Grade: {GRADE}")
print()

# -------------------------------------------
# 2. Inline Conditional Expression
# -------------------------------------------
print("2) Inline Conditional Expression (Ternary Operator)")

# Useful for quick one-line assignments
TEMPERATURE = 17
STATUS = "Cold" if TEMPERATURE < 20 else "Warm"
print(f"Temperature: {TEMPERATURE}°C -> Status: {STATUS}")
print()

# -------------------------------------------
# 3. Data Cleaning with if/elif/else
# -------------------------------------------
print("3) Data Cleaning Example")

data = ["42", "NaN", None, "100", "-5"]
cleaned = []

for item in data:
    if item is None:
        cleaned.append(np.nan)  # Handle missing values
    elif item.lower() == "nan":
        cleaned.append(np.nan)  # Handle string 'NaN'
    elif item.lstrip("-").isdigit():
        cleaned.append(int(item))  # Convert to integer if valid
    else:
        cleaned.append(np.nan)  # Default to NaN for invalid
print("Original:", data)
print("Cleaned :", cleaned)
print()

# -------------------------------------------
# 4. Categorizing Continuous Data
# -------------------------------------------
print("4) Categorizing Continuous Data")

ages = [12, 25, 37, 51, 68]


def categorize_age(age: int) -> str:
    if age < 18:
        return "Child"
    elif age < 40:
        return "Adult"
    elif age < 60:
        return "Middle-aged"
    else:
        return "Senior"


categories = [categorize_age(a) for a in ages]
print("Ages       :", ages)
print("Categories :", categories)
print()

# -------------------------------------------
# 5. Using Conditions in Pandas DataFrames
# -------------------------------------------
print("5) Conditional Logic with Pandas")

# Sample dataset
df = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
        "age": [23, 17, 35, 29, 65],
        "income": [50000, 12000, 72000, 35000, 80000],
    }
)

print("Original DataFrame:\n", df, "\n")

# Example 1: Creating a new column with np.where (vectorized if/else)
df["is_adult"] = np.where(df["age"] >= 18, True, False)
print("With is_adult column:\n", df, "\n")

# Example 2: Categorizing income with nested conditions (vectorized)
df["income_level"] = np.select(
    condlist=[
        df["income"] < 30000,
        df["income"].between(30000, 60000),
        df["income"] > 60000,
    ],
    choicelist=["Low", "Medium", "High"],
    default="Unknown",
)
print("With income_level column:\n", df, "\n")


# Example 3: Applying a custom function (row-wise if/elif/else)
def age_group(row):
    if row["age"] < 18:
        return "Minor"
    elif row["age"] < 60:
        return "Working Age"
    else:
        return "Senior"


df["age_group"] = df.apply(age_group, axis=1)
print("With age_group column:\n", df, "\n")

# -------------------------------------------
# 6. Guard Clauses in Data Pipelines
# -------------------------------------------
print("6) Guard Clauses for Data Validation")


def process_dataset(dataset: pd.DataFrame) -> pd.DataFrame:
    # Guard clause to avoid invalid operations
    if dataset.empty:
        raise ValueError("Dataset is empty.")
    if not {"age", "income"}.issubset(dataset.columns):
        raise KeyError("Missing required columns.")
    # If all checks pass, return a filtered subset
    return dataset[dataset["age"] > 18]


filtered_df = process_dataset(df)
print("Filtered dataset (age > 18):\n", filtered_df, "\n")

# -------------------------------------------
# 7. Complex Conditionals in List Comprehensions
# -------------------------------------------
print("7) Conditions in List Comprehensions")

numbers = range(1, 20)
even_or_odd = [
    "Even" if n % 2 == 0 else "Odd"
    for n in numbers
    if n not in (5, 13)  # Additional filter
]
print("Even/Odd classification (excluding 5 and 13):")
print(even_or_odd)
