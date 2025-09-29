"""
Advanced Tutorial: Assignment Operators in Python
-------------------------------------------------
Assignment operators are used to assign values to variables.
Python supports both simple and augmented assignments.

Operators:
    =     Simple assignment
    +=    Add and assign
    -=    Subtract and assign
    *=    Multiply and assign
    /=    Divide and assign
    //=   Floor-divide and assign
    %=    Modulo and assign
    **=   Exponent and assign
    &=    Bitwise AND and assign
    |=    Bitwise OR and assign
    ^=    Bitwise XOR and assign
    >>=   Right shift and assign
    <<=   Left shift and assign

Key Concepts:
    - Augmented assignment is not just syntactic sugar
    - Mutable vs. immutable objects
    - Operator overloading (__iadd__, __imul__, etc.)
"""

# -------------------------------------------
# 1. Simple Assignment
# -------------------------------------------
print("1) Simple Assignment")

X = 10
print("Initial value of X ->", X)
X = X + 5
print("X after X = X + 5 ->", X)
print()

# -------------------------------------------
# 2. Augmented Assignment (Immutable Types)
# -------------------------------------------
print("2) Augmented Assignment with Immutable Types")

A = 5
print("Initial A id:", id(A))
A += 3  # Equivalent to: a = a + 3
print("A after A += 3 ->", A, " | New id:", id(A))
# Because integers are immutable, a new object is created
print()

# -------------------------------------------
# 3. Augmented Assignment (Mutable Types)
# -------------------------------------------
print("3) Augmented Assignment with Mutable Types")

lst = [1, 2, 3]
print("Initial list:", lst, "| id:", id(lst))
lst += [4, 5]  # In-place extension for lists
print("After lst += [4, 5] ->", lst, "| id:", id(lst))
# Same object is modified because lists are mutable
print()

# -------------------------------------------
# 4. Multiple Assignment
# -------------------------------------------
print("4) Multiple Assignment")

x, y, z = 1, 2, 3
print("x, y, z ->", x, y, z)

# Swapping values without a temporary variable
x, y = y, x
print("Swapped x, y ->", x, y)
print()

# -------------------------------------------
# 5. Chain Assignment
# -------------------------------------------
print("5) Chain Assignment")

B = C = D = 42
print("a, b, c ->", B, C, D)
print("All variables reference the same object id:", id(B), id(C), id(D))
print()

# -------------------------------------------
# 6. Advanced Operators
# -------------------------------------------
print("6) Advanced Operators")

N = 8
print("Initial n ->", N)
N **= 2  # Exponentiation
print("n after n **= 2 ->", N)
N //= 5  # Floor division
print("n after n //= 5 ->", N)
N <<= 2  # Bitwise left shift
print("n after n <<= 2 ->", N)
print()

# -------------------------------------------
# 7. Custom Objects and Operator Overloading
# -------------------------------------------
print("7) Custom Objects with Augmented Assignment")


class Counter:
    """
    Demonstrates operator overloading for augmented assignment.
    Implementing __iadd__ allows in-place addition (+=) to
    modify the object instead of creating a new one.
    """

    def __init__(self, value: int):
        self.value = value

    def __iadd__(self, other):
        print("Custom __iadd__ called")
        self.value += other
        return self  # Returning self enables in-place behavior

    def __repr__(self):
        return f"Counter({self.value})"


counter = Counter(10)
print("Initial counter ->", counter)
counter += 5  # Triggers __iadd__
print("After counter += 5 ->", counter)
print()

# -------------------------------------------
# 8. Using Assignment in Expressions (Python 3.8+)
# -------------------------------------------
print("8) Assignment Expressions (Walrus Operator)")

# The walrus operator (:=) allows assignment inside expressions
if (n := len(lst)) > 3:
    print(f"List length {n} is greater than 3")
print()

# -------------------------------------------
# 9. Mutability Insight
# -------------------------------------------
print("9) Mutability Insight")

# Immutable example
S = "hello"
print("Before += ->", S, "| id:", id(S))
S += " world"
print("After +=  ->", S, "| id:", id(S))  # New id because strings are immutable

# Mutable example
data = {"a": 1}
print("Before |= ->", data, "| id:", id(data))
data |= {"b": 2}  # Dictionary merge (Python 3.9+)
print("After |=  ->", data, "| id:", id(data))  # Same id because dict is mutable
