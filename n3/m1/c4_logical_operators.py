"""
Advanced Tutorial: Logical Operators in Python
-----------------------------------------------
Logical operators combine or negate boolean expressions.

Operators:
    and   -> True if BOTH operands are True
    or    -> True if AT LEAST one operand is True
    not   -> Inverts the boolean value

Key Concepts:
    - Truthy and Falsy Values
    - Short-Circuit Evaluation
    - Custom Boolean Logic with __bool__
"""

# -------------------------------------------
# 1. Basic Logical Operations
# -------------------------------------------
print("1) Basic Logical Operations")

a, b = True, False
print(f"{a} and {b} ->", a and b)  # False: both must be True
print(f"{a} or {b}  ->", a or b)  # True : at least one is True
print(f"not {a}     ->", not a)  # False: negation
print()

# -------------------------------------------
# 2. Truthy and Falsy Values
# -------------------------------------------
print("2) Truthy and Falsy Values")

# Any object can be evaluated in a boolean context
# Falsy: 0, 0.0, '', [], {}, None
# Truthy: almost everything else
values = [0, 1, "", "hello", [], [1], None, {"key": "value"}]
for v in values:
    print(f"bool({repr(v)}) ->", bool(v))
print()

# -------------------------------------------
# 3. Short-Circuit Evaluation
# -------------------------------------------
print("3) Short-Circuit Evaluation")


def expensive_check() -> bool:
    print("expensive_check() called")
    return True


print("Case 1: False and expensive_check() ->")
# 'and' stops if the first operand is False (no need to evaluate the second)
print(False and expensive_check())
print()

print("Case 2: True or expensive_check() ->")
# 'or' stops if the first operand is True
print(True or expensive_check())
print()

# -------------------------------------------
# 4. Logical Operators as Value Returners
# -------------------------------------------
print("4) Logical Operators Return Values, Not Always Booleans")

# In Python, 'and' returns the first falsy value or the last truthy one
print("'hello' and 42 ->", "hello" and 42)  # 42 (both truthy, returns last)
print("'' and 42     ->", "" and 42)  # '' (first falsy)
# 'or' returns the first truthy value
print("'' or 42      ->", "" or 42)  # 42
print("None or 'x'   ->", None or "x")  # 'x'
print()

# -------------------------------------------
# 5. Combining Logical and Relational Operators
# -------------------------------------------
print("5) Combining Logical and Relational Operators")

X = 7
print("(x > 5) and (x < 10) ->", 5 < X < 10)  # True
print("(X < 5) or (X == 7)  ->", (X < 5) or (X == 7))  # True
print("not (X == 7)        ->", X != 7)  # False
print()

# -------------------------------------------
# 6. Custom Objects with __bool__
# -------------------------------------------
print("6) Custom Objects Controlling Truthiness")


class Connection:
    """
    Simulates a network connection whose truth value depends
    on whether it is open.
    """

    def __init__(self, is_open: bool):
        self.open = is_open

    def __bool__(self):
        # Object is considered True if connection is open
        return self.open

    def __repr__(self):
        return f"Connection(open={self.open})"


conn1 = Connection(is_open=True)
conn2 = Connection(is_open=False)

print(f"{conn1} and {conn2} ->", conn1 and conn2)
# conn1 is True, but 'and' returns conn2 (the first falsy value)
print(f"{conn1} or  {conn2} ->", conn1 or conn2)
# conn1 is True, so 'or' returns conn1 immediately
print(f"not {conn2} ->", not conn2)  # True because conn2 is falsy
print()

# -------------------------------------------
# 7. Using Logical Operators in Control Flow
# -------------------------------------------
print("7) Logical Operators in Control Flow")

# Example: lazy default assignment
USERNAME = ""
DEFAULT_USER = "guest"
FINAL_USER = USERNAME or DEFAULT_USER  # 'or' returns default if username is falsy
print("Selected user ->", FINAL_USER)

# Example: guard pattern
data = {"value": 10}
result = data.get("value") and (data["value"] * 2)
print("Computed result ->", result)
