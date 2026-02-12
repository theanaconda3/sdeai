"""
Data types in python: 
1. int -> whole number -> without decimal point +ve, -ve, 0
    3, 4, 13892923, -90, 0, -345
    Infinite possible values for integers.
2. float -> Any number with a decimal point.
    3.14, 2.3, -9.4. 12892.3737, 9.0
    infinite possible values for floating point numbers.
3. string -> anything written inside a double/single quote is called as a string data type.
    "Aravind", "12", '1.23'
    infinite possible values for string data type.
4. boolean -> yes/no -> (sub type of integers)
    True = 1 , False = 0
    Only two possible values for booleans.

print(type(variable_name))
    a = True
    print(type("aravind")) # string
"""

"""
Arithmatic operators (Binary operators): Can be operated between two operands only.
a + b
"""
# a = 10
# b = 20
# print(a + b) # 30
# print(a * b) # 10 * 20 = 200
# print( 5 / 2 ) # 2.5 => division always gives float data type
# print(10 / 2) # 5.0 
# print(5 // 2) # 2
# print( 5 % 2) # % (modulus operator) => reminder = 1
# print( 10 ** 2) # 10^2 => 10 * 10 => 100

# Between two strings we can only use + , * operator
# + => Concatenation => "Abc"+ "Xyz" = "AbcXyz"
# * => second operand always needs to be an integer "abc" * 2 => "abcabc"
# print("Abc" + "Xyz")
# print("abc" * 5) # "abc" + "abc" = "abcabc"

# print(True + 3) # 1 + 3 => 4
# print(False * 10) # 0 * 10 = 0

# print(0.1 + 0.2) # 0.3
# print("A" / "B") # infinite

"""
Homework: 
Given an `n` digit integer, find the sum of all the digits in that integer
124 => 1 + 2 + 4 = 7
"""

# print(True + 3) # Python implicitly converts 'True' to integer => 1 + 3 = 4
# Explicit typecasting: int(), float(), str(), bool()
# print(int(5.4)) # 5
# print(int("5")) # 5
# print(int(float("5.4"))) # 5
# print(int(True)) # 1
# print(int(False)) # 0

# "", 0, 0.0 => False
# remaining all are treated as True
# print(bool(0.0))

num = int(input("Enter a number:")) # "35" => integer
print(num, type(num)) # 35, int