# Variables in Python

## What is a Variable

- A variable is a **name** that refers to an object (value) in memory.
- Variables are created **when a value is assigned** using `=`.
- Python variables are **dynamically typed** (no type declaration needed).

Example:

```python
x = 10
name = "Alice"
```

## Rules for Naming Variables

- Must start with a letter (a–z, A–Z) or an underscore (\_)
- Can contain letters, numbers, and underscores
- Case-sensitive (age ≠ Age)
- Cannot be a Python keyword

```python
# Valid variable names
age = 25
_name = "test"
total_sum = 100

# Invalid variable names
2value = 10      # starts with number
total-sum = 5    # hyphen not allowed
class = 3        # keyword
```

## Naming Conventions (Recommended)

- Use snake_case for naming variables in python (not standard but recommended)
- Other naming styles can be camelCase(eg. java, javascript), PascalCase (for naming classes, interfaces etc.. in java, javascript)

```python
full_name = "Aravind Samudrala"
```

# Data types in python

- Every data type in python has three properties : type, value & identifier(memory address where it's stored)

## Integer (`int`)

- Represents **whole numbers** (positive, negative, zero)

Example:

```python
a = 10
b = -5
c = 12345678901234567890
```

## Float (`float`)

- Represents decimal numbers.
- Values are approximate, not exact

```python
x = 3.14
y = 0.1 + 0.2   # 0.30000000000000004
```

## Strings (`str`)

- Represents text with zero or more characters.
- Immutable (cannot be changed after creation).
- Can be accessed with zero based indexing.

```python
name = "Aravind"
print(len(name)) # prints the number of characters i.e 7
print(name[0]) # prints the first character in the sequence i.e 'A'
name[0] = 'S' # invalid statement throws exception.
```

# Arithmatic Operators in python

## List of Arithmetic Operators

| Operator | Name           | Description                     |
| -------- | -------------- | ------------------------------- |
| `+`      | Addition       | Adds two values                 |
| `-`      | Subtraction    | Subtracts right value from left |
| `*`      | Multiplication | Multiplies two values           |
| `/`      | Division       | Returns float division result   |
| `//`     | Floor Division | Returns quotient rounded down   |
| `%`      | Modulus        | Returns remainder               |
| `**`     | Exponentiation | Raises power                    |

## Eligible Data Types for Arithmetic Operations

### Integer (`int`)

- Supports **all arithmetic operators**
- Results are exact (except `/`)

Example:

```python
a = 10
b = 3

a + b    # 13
a / b    # 3.333...
a // b   # 3
a % b    # 1
a ** b   # 1000
```

## Floating Point (float)

- Supports all arithmetic operators
- Results are approximate

```python
x = 5.5
y = 2.0

x + y    # 7.5
x // y   # 2.0

```

## Boolean (bool)

- Treated as integers (True = 1, False = 0)
- Supports all arithmetic operators

```python
True + True     # 2
False * 10      # 0
True ** False   # 1
```

## Mixed Numeric Types (int, float, bool)

- Automatic type promotion:
- bool → int → float

```python
1 + 2.5 # float
True + 2 # int
```

# Type casting

## Explicit Type Casting

- Done **manually by the programmer**
- Use **built-in functions** to convert values between types

### Common Type Casting Functions

| Function  | Description         | Example            |
| --------- | ------------------- | ------------------ |
| `int()`   | Converts to integer | `int(3.7)` → 3     |
| `float()` | Converts to float   | `float(5)` → 5.0   |
| `str()`   | Converts to string  | `str(100)` → "100" |
| `bool()`  | Converts to boolean | `bool(0)` → False  |
