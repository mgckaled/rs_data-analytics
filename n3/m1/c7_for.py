"""
Advanced Tutorial: for Loops in Data Analysis
---------------------------------------------
The for loop is fundamental for:
    - Iterating over datasets
    - Cleaning and transforming data
    - Generating new features
    - Running simulations and aggregations

Key Concepts:
    - Iterating over sequences and iterables
    - Enumerating with indexes
    - Dictionary and nested iterations
    - Looping over pandas DataFrames
    - List/Dict comprehensions
    - Vectorized alternatives for performance
"""

import numpy as np
import pandas as pd

# -------------------------------------------
# 1. Basic Iteration over Lists
# -------------------------------------------
print("\n1) Basic Iteration over Lists")

values = [3, 7, 12, 18, 25]
for v in values:
    print(f"Value: {v}, Squared: {v**2}")
print()

# -------------------------------------------
# 2. Using enumerate() for Index + Value
# -------------------------------------------
print("2) Using enumerate() for Index and Value")

for idx, v in enumerate(values, start=1):
    print(f"Row {idx}: Value={v}")
print()

# -------------------------------------------
# 3. Iterating over Dictionaries
# -------------------------------------------
print("3) Iterating over Dictionaries")

data_dict = {"Alice": 85, "Bob": 72, "Charlie": 90}
for name, score in data_dict.items():
    LABEL = "Pass" if score >= 75 else "Fail"
    print(f"{name}: {score} -> {LABEL}")
print()

# -------------------------------------------
# 4. Nested Loops for Data Transformation
# -------------------------------------------
print("4) Nested Loops Example")

matrix = [[1, 2, 3], [4, 5, 6]]
flattened = []
for row in matrix:
    for element in row:
        flattened.append(element * 2)
print("Flattened and doubled:", flattened)
print()

# -------------------------------------------
# 5. Looping Through a Pandas DataFrame
# -------------------------------------------
print("5) Looping Through a Pandas DataFrame")

df = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [23, 17, 35],
        "income": [50000, 12000, 72000],
    }
)

print("Original DataFrame:\n", df, "\n")

# Example 1: iterrows() (row-wise)
print("Using iterrows():")
for idx, row in df.iterrows():
    print(f"{row['name']} -> Age: {row['age']}, Income: {row['income']}")
print()

# Example 2: itertuples() (faster, named tuples)
print("Using itertuples():")
for row in df.itertuples(index=False):
    print(f"{row.name} -> Age: {row.age}, Income: {row.income}")
print()

# Example 3: Vectorized Alternative (Preferred for Performance)
print("Vectorized Example:")
# Add a new column without explicit Python loops
df["income_category"] = np.where(df["income"] > 40000, "High", "Low")
print(df, "\n")

# -------------------------------------------
# 6. Looping with Conditional Logic
# -------------------------------------------
print("6) Looping with Conditional Logic")

ages = [12, 25, 37, 51, 68]
adult_ages = []
for age in ages:
    if 18 <= age <= 60:
        adult_ages.append(age)
print("Adults (18-60):", adult_ages)
print()

# -------------------------------------------
# 7. List Comprehensions for Data Transformation
# -------------------------------------------
print("7) List Comprehensions")

# Transform and filter in one line
squared_evens = [x**2 for x in values if x % 2 == 0]
print("Squared even numbers:", squared_evens)
print()

# -------------------------------------------
# 8. Dictionary Comprehensions
# -------------------------------------------
print("8) Dictionary Comprehensions")

score_labels = {
    name: ("Pass" if score >= 75 else "Fail") for name, score in data_dict.items()
}
print("Score labels:", score_labels)
print()

# -------------------------------------------
# 9. Combining for with zip()
# -------------------------------------------
print("9) Iterating with zip()")

names = ["Alice", "Bob", "Charlie"]
scores = [85, 72, 90]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
print()

# -------------------------------------------
# 10. Looping with break and continue
# -------------------------------------------
print("10) Using break and continue")

for v in values:
    if v < 5:
        continue  # Skip values less than 5
    if v > 20:
        print("Stopping loop at value:", v)
        break
    print("Processed value:", v)
print()

# -------------------------------------------
# 11. Complex Data Aggregation Example
# -------------------------------------------
print("11) Aggregating Data with for Loop")

dataset = [12, 15, np.nan, 20, 22, None, 18]
cleaned = []
for item in dataset:
    if item is None or (isinstance(item, float) and np.isnan(item)):
        continue  # Skip missing values
    cleaned.append(item)

mean_value = sum(cleaned) / len(cleaned)
print("Cleaned Data:", cleaned)
print("Mean Value :", mean_value)
print()

# -------------------------------------------
# 12. Guarding Performance: When to Avoid Python Loops
# -------------------------------------------
print("12) Performance Guard")

large_array = np.random.randint(0, 100, size=1_000_000)

# Vectorized mean (preferred)
vectorized_mean = large_array.mean()

# Manual mean (much slower in Python)
# manual_mean = sum(large_array) / len(large_array)  # Not recommended

print("Vectorized mean:", vectorized_mean)
print("Note: Avoid Python for-loops for large arrays; prefer NumPy/pandas.")
