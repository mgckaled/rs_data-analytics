"""
==========================================================
Understanding the `while` Loop in Data Analysis
==========================================================

The `while` loop repeatedly executes a block of code
*as long as* a given condition evaluates to True.

General syntax:
----------------
while condition:
    # code to execute
    # update variables to eventually break the loop

Key Concepts:
-------------
1. The loop continues UNTIL the condition becomes False.
2. If the condition never becomes False -> Infinite Loop.
3. Useful when the number of iterations is unknown beforehand.
4. Requires careful state updates inside the loop.

This script demonstrates:
- Iterative data cleaning until a stopping criterion is met
- Real-time data simulation
- Convergence of numerical calculations
- Safe break conditions to avoid infinite loops
"""

import random
import time

import numpy as np
import pandas as pd

# --------------------------------------------------------
# Configuration constants (UPPER_CASE)
# --------------------------------------------------------
RNG_SEED = 42
LOC = 50
SCALE = 10
SAMPLE_SIZE = 100
ADDED_OUTLIERS = [200, 250]
VALUE_COL = "value"

THRESHOLD = 3  # Z-score threshold for outlier detection
MAX_POINTS = 5  # buffer size for simulated stream
SLEEP_INTERVAL = 0.2  # seconds, simulate delay between stream points

TARGET = 2025  # target value for sqrt approximation
TOLERANCE = 1e-6  # convergence tolerance for numerical method

DESIRED_MEAN = 60  # stopping condition for mean-driven fetch
MAX_ITERATIONS = 20  # maximum iterations in data fetching loop

# --------------------------------------------------------
# 0. Deterministic setup
# --------------------------------------------------------
np.random.seed(RNG_SEED)
random.seed(RNG_SEED)

# --------------------------------------------------------
# 1. Iterative Outlier Removal
# --------------------------------------------------------
print("\n[1] Iterative Outlier Removal")
print("--------------------------------")

data = np.random.normal(loc=LOC, scale=SCALE, size=SAMPLE_SIZE).tolist()
data.extend(ADDED_OUTLIERS)  # Add strong outliers
df = pd.DataFrame({VALUE_COL: data})

ITERATION = 0

while True:
    ITERATION += 1
    mean_val = df[VALUE_COL].mean()
    std_val = df[VALUE_COL].std(ddof=0)  # population std for consistency
    if std_val == 0 or df.empty:
        # safety guard: no variation or empty frame
        print("No variation or empty DataFrame. Stopping.")
        break

    z_scores = (df[VALUE_COL] - mean_val) / std_val
    outliers = df[np.abs(z_scores) > THRESHOLD]
    print(f"Iteration {ITERATION}: {len(outliers)} outliers found")

    if outliers.empty:
        print("No more outliers detected. Cleaning complete.\n")
        break  # Exit loop when condition is met

    # Remove detected outliers and continue
    df = df[np.abs(z_scores) <= THRESHOLD]

# --------------------------------------------------------
# 2. Real-Time Data Simulation
# --------------------------------------------------------
print("[2] Real-Time Data Simulation")
print("--------------------------------")

buffer = []

while len(buffer) < MAX_POINTS:
    new_value = random.randint(0, 100)
    buffer.append(new_value)
    print(f"Collected value: {new_value} | Buffer size: {len(buffer)}")
    time.sleep(SLEEP_INTERVAL)  # Simulate real-time delay

print(f"Final buffer: {buffer}\n")

# --------------------------------------------------------
# 3. Convergence Example: Root Approximation (Newton-Raphson)
# --------------------------------------------------------
print("[3] Numerical Convergence: Square Root Approximation")
print("--------------------------------")

GUESS = TARGET / 2
ITERATION = 0

while True:
    ITERATION += 1
    # Newton-Raphson update
    NEW_GUESS = 0.5 * (GUESS + TARGET / GUESS)
    if abs(NEW_GUESS - GUESS) < TOLERANCE:
        GUESS = NEW_GUESS
        break  # Converged
    GUESS = NEW_GUESS

print(f"Square root of {TARGET} ≈ {GUESS:.6f} (iterations: {ITERATION})\n")

# --------------------------------------------------------
# 4. Multi-Condition Data Fetching
# --------------------------------------------------------
print("[4] Multi-Condition Data Fetching")
print("--------------------------------")

collected = []
ITERATION = 0

while (
    np.mean(collected) if collected else 0
) < DESIRED_MEAN and ITERATION < MAX_ITERATIONS:
    ITERATION += 1
    value = random.randint(0, 100)
    collected.append(value)
    print(
        f"Iter {ITERATION:02d}: Added {value}, Current Mean: {np.mean(collected):.2f}"
    )

print("\nLoop ended because:")
if np.mean(collected) >= DESIRED_MEAN:
    print("- Desired mean reached.")
else:
    print("- Maximum iterations reached.")
