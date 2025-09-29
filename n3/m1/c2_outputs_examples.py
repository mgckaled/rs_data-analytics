# -*- coding: utf-8 -*-
"""
Module: Python Output Examples
Demonstrates different ways to output data in Python,
from basic prints to formatted and advanced outputs.

Author: Marcel Kaled
Date: 2025-09-24
Version: 1.0
"""


def basic_print() -> None:
    """
    Basic output using the print function.
    """
    print("Hello, world!")  # Simple string output
    print(42)  # Outputting an integer
    print(3.1415)  # Outputting a float
    print(True)  # Outputting a boolean
    print()  # Empty line for separation


def print_multiple_values() -> None:
    """
    Printing multiple values in a single statement.
    """
    name: str = "Alice"
    age: int = 30
    print("Name:", name, "Age:", age)  # Comma-separated values
    print(f"{name} is {age} years old")  # Formatted string (f-string)
    print(f"{name} | Age: {age}", sep=" | ")  # Using custom separator
    print()  # Empty line


def print_with_formatting() -> None:
    """
    Using advanced formatting options for output.
    """
    value: float = 1234.56789

    # Number formatting
    print(f"Default: {value}")
    print(f"Two decimals: {value:.2f}")
    print(f"Scientific notation: {value:.2e}")

    # Padding and alignment
    print(f"Right aligned: {value:>10.2f}")
    print(f"Left aligned: {value:<10.2f}")
    print(f"Centered: {value:^10.2f}")

    # Using format() function
    print(f"Using format(): {value:.1f}")
    print()


def print_collections() -> None:
    """
    Printing collections such as lists and dictionaries.
    """
    fruits: list[str] = ["apple", "banana", "cherry"]
    person: dict[str, any] = {"name": "Bob", "age": 25, "city": "NY"}

    # Printing list
    print("Fruits:", fruits)
    for fruit in fruits:
        print(f"- {fruit}")

    # Printing dictionary
    print("Person Info:")
    for key, value in person.items():
        print(f"  {key}: {value}")

    print()


def advanced_output() -> None:
    """
    Advanced output using unpacking, end and flush.
    """
    numbers: list[int] = [1, 2, 3, 4, 5]

    # Using unpacking
    print("Numbers:", *numbers, sep=", ")

    # Printing on same line
    for number in numbers:
        print(number, end=" ")
    print()  # Line break

    # Real-time output
    for number in numbers:
        print(number, end=" ", flush=True)
    print()


def main() -> None:
    """
    Main function demonstrating all types of output.
    """
    print("=== Basic Print ===")
    basic_print()

    print("=== Multiple Values ===")
    print_multiple_values()

    print("=== Formatted Output ===")
    print_with_formatting()

    print("=== Collections ===")
    print_collections()

    print("=== Advanced Output ===")
    advanced_output()


# --- Entry Point ---
if __name__ == "__main__":
    main()
