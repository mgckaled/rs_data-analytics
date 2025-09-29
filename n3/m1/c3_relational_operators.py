"""
Advanced Tutorial: Relational Operators in Python
--------------------------------------------------
Relational (or comparison) operators are used to compare two values.
They return a boolean value: True or False.

Operators:
    ==   Equal
    !=   Not equal
    <    Less than
    <=   Less than or equal to
    >    Greater than
    >=   Greater than or equal to
"""

# -------------------------------------------
# 1. Basic Comparisons
# -------------------------------------------
from functools import total_ordering

a, b = 10, 20
print("1) Basic Comparisons")
print(f"{a} == {b} ->", a == b)  # False: 10 is not equal to 20
print(f"{a} != {b} ->", a != b)  # True: 10 is different from 20
print(f"{a} < {b}  ->", a < b)  # True: 10 is less than 20
print(f"{a} <= {b} ->", a <= b)  # True
print(f"{a} > {b}  ->", a > b)  # False
print(f"{a} >= {b} ->", a >= b)  # False
print()

# -------------------------------------------
# 2. Comparisons with Different Data Types
# -------------------------------------------
print("2) Cross-Type Comparisons")
# Numbers of different types can be compared if logically compatible
# True: float vs int, Python converts internally
print("3.0 == 3 ->", 3.0 == 3)
# Strings are compared lexicographically (dictionary order)
print("'apple' < 'banana' ->", "apple" < "banana")  # True
# Lists and tuples compare element by element
print("[1, 2] < [1, 3] ->", [1, 2] < [1, 3])  # True
print()

# -------------------------------------------
# 3. Boolean Shortcuts and Intrinsic Concepts
# -------------------------------------------
print("3) Boolean Shortcuts")
# Chained comparisons are allowed and evaluated left to right
X = 5
print("1 < x < 10 ->", 1 < X < 10)  # True: equivalent to (1 < x) and (x < 10)
# 'is' checks identity, not equality
# True (but don't rely on this for numbers beyond cache)
print("x is 5 ->", X is 5)
print("x == 5 ->", X == 5)  # True (value comparison)
print()

# -------------------------------------------
# 4. Custom Objects and Magic Methods
# -------------------------------------------
print("4) Custom Object Comparisons")


class Version:
    """
    A class to represent a software version.
    Demonstrates how to implement custom comparison behavior
    using rich comparison methods (__eq__, __lt__, etc.).
    """

    def __init__(self, major: int, minor: int):
        self.major = major
        self.minor = minor

    def __eq__(self, other):
        # Equality based on both major and minor numbers
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        # Lexicographic comparison: first major, then minor
        return (self.major, self.minor) < (other.major, other.minor)

    def __repr__(self):
        return f"Version({self.major}, {self.minor})"


v1 = Version(1, 4)
v2 = Version(1, 10)
v3 = Version(1, 4)

print(f"{v1} == {v2} ->", v1 == v2)  # False
print(f"{v1} <  {v2} ->", v1 < v2)  # True
print(f"{v1} == {v3} ->", v1 == v3)  # True (same major and minor)
print()

# -------------------------------------------
# 5. Sorting with Custom Comparisons
# -------------------------------------------
print("5) Sorting Objects Using Relational Operators")
versions = [v2, v1, v3]
print("Unsorted:", versions)
print("Sorted:", sorted(versions))  # Uses __lt__ internally
print()

# -------------------------------------------
# 6. Intrinsic Concept: Total Ordering
# -------------------------------------------
print("6) Total Ordering Example")


@total_ordering
class Person:
    """
    Using @total_ordering allows you to define only __eq__ and one
    other comparison (like __lt__), and Python will automatically
    provide the rest.
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return f"{self.name}({self.age})"


p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(f"{p1} > {p2} ->", p1 > p2)  # True, because 30 > 25
print(f"{p1} >= {p2} ->", p1 >= p2)  # True, generated automatically
print(f"{p1} == {p2} ->", p1 == p2)  # False
