
"""
Boolean is a sub data type of integer : True = 1, False = 0

== 
    => Equality operator, can be used between any two data types.
    => result of this operator is always a boolean.
    => we can compare any two data types.
    => (int, int), (bool, float), (int, float), (string, string)
!= 
    => Reverse of equality.

> , < , >= , <= : (numbers) => integers, float, boolean
    => These operators can be used between any numeric datatypes.
    => These operators can be used between any two strings.
"""

# ASCII values => Every character in memory is represented as a number. 
# ["a", "z"] = [97, 122]
# ["A", "Z"] = [65, 90]
# ["0", "9"] = [48, 57]

# str = "abcz86" => { 97, 98, 99, 122, 56, 54 }

# print("ab" > "Ab") # {97 > 65}
# aravind , ajay 
# "abc" < "abcd"
# print("abc" >= "abc") # 1 < 1


"""
Logical operators: 
and, or: Binary operators : O1 and O2 , O1 or O2

and : If both the operands are true then the result is true
O1      O2      O1 and O2
True    True        True
True    False       False
False   True        False
False   False       False

- If the first operand is true then the result of and operation is equal to second operand. 
- If the first operand is a false then the result of the and operation is equal to first operand.

or : If atleast one operand is True then the result True.
O1      O2          O1 or O2
True    True        True
True    False       True
False   True        True
False   False       False

- If the first operand is a true then the result is equal to first operand itself. 
- If the first operand is a false then the result is equal to second operand.

not: Unary opertor !True = False, !False = True
"""
# and , or, not these are keywords in python. 

"""
Logical operators can work between any two data types.

Falsy : False, 0, 0.0, "", [], {}, (), None
Truthy : All values other than Falsy values are Truthy values.
"""

# 1 and 3 => True and True
# print(None and "aravind") # False 

# print(None or False) # False

# print(not "aravind") # False
# print(not None) # True

"""
3 conditional statements: 
if: If the given condition is truthy then the block of code executes otherwise no.
elif: Can be used right after and `if` statement or another `elif` statement.
else: can be placed right after an if statement or elif statement.Won't take any condition as input.
"""

# num = 33
# if num % 2 == 0:
#     print("Even number")
# elif num % 2 == 1:
#     print("Odd number")

# [0, 100] : A (90+) , B (50+), C (<50)
# marks = 98
# if marks >= 90:
#     print("A")
# elif marks >= 50:
#     print("B")
# elif marks < 50:
#     print("C")

# gender = "M" # M, F, O
# if gender == "M": 
#     print("Male")
# elif gender == "F":
#     print("Female")
# elif gender == "O": 
#     print("others")

# if 10 % 2 == 0:
#     print("Inside if")
# else:
#     print("inside else")

# if c1, elif c2, elif c3, elif c4 .... elif cn, else
# In an if, elif, else ladded always a single block gets executed.


"""
Loops: 
while, for
Loops are used to execute a block of code repeatedly.
"""

# num = 0 # 0 -> 1 -> 2 -> 3
# while num < 3: # 0 < 3, 1 < 3, 2 < 3, 3 < 3
#     print(num) # 0, 1, 2 
#     num = num + 1 
# print("Program ended", num) # 

# for range(start, end, step) => [start, end)
# print(range(0, 5, 1)) # { 0, 1, 2, 3, 4 }
# in is used to check if a value is in a given range or not 
# print(1 in range(0, 5, 2)) # { 0, 2, 4 }

# { 0, 1, 2, 3, 4 }
#.              x
# for x in range(0, 5, 3):
#     print(x) # 0, 1, 2, 3, 4

# for x in "aravind": # { 'a', 'r', 'a', 'v', 'i', 'n', 'd'}
#     print(x)

# HW: Find the number of small alphabets in a given string. Ex: "AraVInd" => 4
# HW: Find the sum of even digits in a given integer. Ex: 871902 => 8 + 0 + 2 = 10
# HW: Find if a given string is palindrome or not. Ex: "eye" , "madam"