"""
==========================================================
Working with Strings in Python for Data Analysis
==========================================================

This script demonstrates:
- Basic string operations (indexing, slicing, immutability)
- Cleaning and normalization for datasets
- Parsing structured information
- Advanced formatting (f-strings, join, split)
- Regular expressions for pattern matching
"""

import re
from io import StringIO

import numpy as np
import pandas as pd

# --------------------------------------------------------
# Configuration constants
# --------------------------------------------------------
RANDOM_SEED = 42
RAW_TEXT = "   Data Science is powerful!   "
MESSY_NAMES = ["   ALICE  ", "BoB", "charlie  ", "DaViD"]
CSV_TEXT = """id,name,score
1,Alice,89
2,Bob,95
3,Charlie,78
4,David,92
"""

TARGET_PATTERN = r"[A-Z][a-z]+"
REPLACEMENT_WORD = "ANALYTICS"
TARGET_CHAR = "a"

# --------------------------------------------------------
# 1. Basic String Properties
# --------------------------------------------------------
print("\n[1] Basic String Properties")
print("--------------------------------")
print(f"Original text: '{RAW_TEXT}'")
print(f"Length: {len(RAW_TEXT)}")
print(f"First character: '{RAW_TEXT[0]}'")
print(f"Last 5 characters: '{RAW_TEXT[-5:]}'")
print(f"Reversed text: '{RAW_TEXT[::-1]}'")
# Demonstrating immutability: create a new string instead of modifying in place
CLEAN_TEXT = RAW_TEXT.strip()
print(f"Trimmed text: '{CLEAN_TEXT}'")

# --------------------------------------------------------
# 2. Case Normalization and Replacement
# --------------------------------------------------------
print("\n[2] Case Normalization and Replacement")
print("--------------------------------")
UPPER_TEXT = CLEAN_TEXT.upper()
LOWER_TEXT = CLEAN_TEXT.lower()
REPLACED_TEXT = CLEAN_TEXT.replace("powerful", REPLACEMENT_WORD)
print(f"Upper case : {UPPER_TEXT}")
print(f"Lower case : {LOWER_TEXT}")
print(f"Replaced   : {REPLACED_TEXT}")

# Count occurrences of a character
COUNT_A = CLEAN_TEXT.lower().count(TARGET_CHAR)
print(f"Occurrences of '{TARGET_CHAR}': {COUNT_A}")

# --------------------------------------------------------
# 3. Cleaning Data in a Pandas Series
# --------------------------------------------------------
print("\n[3] Cleaning Names in a DataFrame")
print("--------------------------------")
np.random.seed(RANDOM_SEED)
names_df = pd.DataFrame({"raw_name": MESSY_NAMES})

names_df["clean_name"] = (
    names_df["raw_name"]
    .str.strip()
    .str.title()  # Proper case: First letter upper, rest lower
)
print(names_df)

# --------------------------------------------------------
# 4. Parsing CSV Text
# --------------------------------------------------------
print("\n[4] Parsing CSV Text")
print("--------------------------------")


csv_df = pd.read_csv(StringIO(CSV_TEXT))
print(csv_df)

# Extract initials from names using vectorized string operations
csv_df["initial"] = csv_df["name"].str[0]
print("\nWith initials:")
print(csv_df)

# --------------------------------------------------------
# 5. Regular Expressions for Pattern Matching
# --------------------------------------------------------
print("\n[5] Regular Expressions")
print("--------------------------------")
pattern_matches = re.findall(TARGET_PATTERN, CLEAN_TEXT)
print(f"Words starting with capital letters: {pattern_matches}")

# Replace all capitalized words with a placeholder
placeholder_text = re.sub(TARGET_PATTERN, "X", CLEAN_TEXT)
print(f"Placeholder replacement: {placeholder_text}")

# --------------------------------------------------------
# 6. Advanced Formatting and Joining
# --------------------------------------------------------
print("\n[6] Advanced Formatting and Joining")
print("--------------------------------")
values = [10, 20, 30]
FORMATTED = ", ".join([f"${v:.2f}" for v in values])
print(f"Joined price list: {FORMATTED}")

# Dynamic f-string with calculations
mean_score = csv_df["score"].mean()
print(f"Average score across students: {mean_score:.2f}")

# --------------------------------------------------------
# 7. Multi-Line Strings and Dedentation
# --------------------------------------------------------
print("\n[7] Multi-Line Strings")
print("--------------------------------")
MULTI_LINE = (
    "Data Cleaning Steps:\n"
    "- Trim whitespace\n"
    "- Normalize case\n"
    "- Handle missing values"
)
print(MULTI_LINE)
