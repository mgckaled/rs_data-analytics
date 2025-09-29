# -*- coding: utf-8 -*-
"""
Module: Customer Data Processing
Demonstrates advanced commenting, type hints, and professional Python practices.

Author: Marcel Kaled
Date: 2025-09-24
Version: 1.1
"""


class Customer:
    """
    Customer class
    Represents basic customer information.

    Attributes:
        name (str): Full name of the customer
        age (int): Customer's age in years
        email (str): Customer's email address
    """

    def __init__(self, name: str, age: int, email: str):
        # Private attributes with underscore convention
        self._name = name
        self._age = age
        self._email = email

    @property
    def name(self) -> str:
        """Public getter for the customer's name"""
        return self._name

    @property
    def age(self) -> int:
        """Public getter for the customer's age"""
        return self._age

    @age.setter
    def age(self, value: int):
        """
        Setter for customer's age
        Ensures the provided value is positive.

        Args:
            value (int): New age of the customer

        Raises:
            ValueError: if value <= 0
        """
        if value <= 0:
            raise ValueError("Age must be positive")
        self._age = value

    @property
    def email(self) -> str:
        """Public getter for the customer's email"""
        return self._email


def filter_customers_by_age(customers: list[Customer], min_age: int) -> list[Customer]:
    """
    Filters customers with age equal or greater than min_age.

    Args:
        customers (List[Customer]): List of Customer objects
        min_age (int): Minimum age for filtering

    Returns:
        List[Customer]: List of filtered customers
    """
    return [c for c in customers if c.age >= min_age]


def customer_report(customers: list[Customer]) -> None:
    """
    Generates a simple customer report.

    Args:
        customers (List[Customer]): List of customers to display
    """
    print("=== Customer Report ===")
    for customer in customers:
        # Use public properties, avoiding access to protected members
        print(f"{customer.name} - {customer.age} years old - {customer.email}")


# --- Usage Example ---
if __name__ == "__main__":
    # Creating example customers
    example_customers = [
        Customer("Alice Silva", 30, "alice@email.com"),
        Customer("Bruno Costa", 22, "bruno@email.com"),
        Customer("Carla Souza", 40, "carla@email.com"),
    ]

    # Filtering customers aged 25 or older
    older_customers = filter_customers_by_age(example_customers, 25)

    # Generating final report
    customer_report(older_customers)
