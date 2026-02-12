## I. Comparison Operators

Comparison operators evaluate the relationship between two operands and return a Boolean (`True` or `False`).

| Operator | Name             | Example            |
| :------- | :--------------- | :----------------- |
| `==`     | Equal            | `5 == 5.0` (True)  |
| `!=`     | Not Equal        | `5 != 4` (True)    |
| `>`      | Greater Than     | `"b" > "a"` (True) |
| `<`      | Less Than        | `2 < 5` (True)     |
| `>=`     | Greater or Equal | `5 >= 5` (True)    |
| `<=`     | Less or Equal    | `4 <= 5` (True)    |

### Edge Cases: Comparison

1. **Implicit Numeric Coercion**: `bool`, `int`, and `float` are cross-compatible.
   - `True == 1` and `False == 0.0` are both `True`.
2. **String Lexicographical Order**: Based on Unicode (UTF-8) code points.
   - **Case Sensitivity**: `"Z" < "a"` is `True` (Uppercase 65-90 < Lowercase 97-122).
   - **Prefix Rule**: If one string is a prefix of another, the shorter string is smaller. `"abc" < "abcd"` is `True`.
   - **Numeric Strings**: `"10" < "2"` is `True` because it compares the first character `'1'` vs `'2'`.
3. **Incompatible Types**:
   - `5 > "3"` raises a `TypeError`.
   - `5 == "5"` evaluates to `False` (No error, just not equal).

---

## II. Logical Operators

Used to combine conditional statements. These use **Short-Circuit Evaluation**.

| Operator | Logic                                | Result                      |
| :------- | :----------------------------------- | :-------------------------- |
| `and`    | Returns True if both are true        | `True and False` -> `False` |
| `or`     | Returns True if at least one is true | `False or True` -> `True`   |
| `not`    | Inverts the Boolean result           | `not True` -> `False`       |

### Edge Cases: Logical Operators

1. **Short-Circuiting**:
   - `and`: If the first operand is `False`, the second is **never evaluated**.
   - `or`: If the first operand is `True`, the second is **never evaluated**.
   - _Example_: `False and print("Hello")` will print nothing.
2. **Return Values (Non-Boolean)**: In Python, `and` and `or` don't always return `True/False`; they return one of the actual operands.
   - `x or y`: Returns `x` if `x` is truthy, else returns `y`.
   - `x and y`: Returns `x` if `x` is falsy, else returns `y`.
   - _Example_: `"" or "Default"` returns `"Default"`.
3. **Truthiness**:
   - **Falsy**: `0`, `0.0`, `""`, `[]`, `{}`, `()`, `None`, `False`.
   - **Truthy**: Any non-zero number, non-empty string, or populated collection.
4. **Operator Precedence**:
   - Order: `not` > `and` > `or`.
   - _Example_: `True or True and False` evaluates to `True` because `and` runs first. Use `()` to force order.
5. **Chained Comparisons**: Python allows `1 < x < 10`, which is shorthand for `(1 < x) and (x < 10)`.

# Conditional Statements

Conditional statements allow you to execute specific blocks of code based on whether a condition is `True` or `False`. Python uses **indentation** (usually 4 spaces) to define the scope of these blocks.

The `if`, `elif` (short for else if), and `else` keywords form the logic chain.

```python
x = 10

if x > 15:
    print("Greater than 15")
elif x == 10:
    print("Exactly 10")  # This runs
else:
    print("Something else")
```

### Ternary operator ( A shorthand for if,else statement)

```python
print("Even" if 10 % 2 == 0 else "odd")
```

# Loops

## range() function

```python
range(start, stop, step)
```

## for loop

```python
for i in range(0, 3):
    doSomething..
```

## While loop

```python
while condition:
    doSomething ..
```

## Loop control statements

`continue`:
`break`:
`pass`:
