"""
Lists: 
Primitive data types: int, float, boolean, string
2L -> Name1, Name2, Name3 .... Namen
"Aravind"
"Rajesh"

Non primitive data types: We can organize mutlple data types in a single variable.
names = [va1, val2, val3 ... valn]
"""

# names = ["Aravind", "Rajesh", "Shruthi"]
# print(type(names)) # list
# print(len(names))

# Lists in python or ordered, mutable (can be modified).

# indexing in lists: index means position. 
# names = ["Aravind", "Rajesh", "Shruthi"]
# #            0          1         2         => Positive indexing.
# #           -3          -2        -1
# print(names[1], names[-2]) # Rajesh Rajesh
# names[1] = "Santosh" # Update value at index 1 to "Santosh"
# print(names[1], names[-2]) # Santosh Santosh

# a = 10
# a = 12 (Updating the entire value of the variable)

# a = [1, 3, 4] # list
# a = 345 # int (updating the entire value of the variable)

# a = [3, 4 , 5]
# a[1] = 90 # We are updating the data of the list and not the whole variable.

# Lists in python are heterogenious in nature.
# nums = [3, 4.3, "Aravind", True, [0, 9, 8], [3, 4, 6]]
# #       0   1       2       3        4          5
# print(nums[-1][-1]) # [3, 4, 6]

# Lists are mutable: add, delete, update elements from a list. 
# nums = [3, 8, 19, 89] # append => add new element at the end of the list
# [3, 8, 19, 89].append("Aravind") => [3, 8, 19, 89, "Aravind"]
# print(nums)
# nums.append("Aravind")
# print(nums)
# human => play, workout, eat, walk, code
# [3, 8, 19, 89] => [3, 8, 19, "Aravind", 89]
# nums.insert(3, "Aravind")
# print(nums)
# deleted_value = nums.pop(2) # [3, 8, 19, 89]  => [3, 8, 89] 
# print(deleted_value, nums)
# deleted_value = nums.pop(1)
# print(nums, deleted_value)
# nums = [3, 8, 19, 89]
# del nums # deletes the element at index 1
# print(nums)

"""
Iteration through list: 
Sequence data types: "Aravind", [3, 4, 5], range(start, end, step)

for loop:
"""
# name = "Aravind"
# name[0] = "X" # Strings are immutable.
# print(name[0])

# name = "Aravind"
# # for-in loop
# for char in name: # char = {'A', 'r', 'a', 'v', 'i', 'n', 'd'}
#     print(char)

# names = ["Aravind", "Rajesh", "Shruthi"]
# print(names[2][-2]) # "Shruthi"
#                                       index=3
# # for-in loop
# for name in names: # name =  {"Aravind", "Rajesh", "Shruthi"}
#     print(name)
# index = 0 # 0 -> 1 -> 2
# while index < len(names): # 0 < 3, 1 < 3, 2 < 3, 3 < 3
#     print(names[index]) # names[2] = "Shruthi"
#     index += 1

# Tuples -> sequence data structure which pretty similar to lists. 
# Common: indexing, iteration (as tuple is also a sequence), heterogenious in nature.
# Lists are mutable whereas tuples are immutable.

# scores = (12, 34, 55, 78)
# #          0.  1   2   3
# #         -4  -3  -2  -1
# print(scores[-9])


"""
Sequence data types: string, list, tuple
Slicing: 

"abcd" => slice is like a subsequence. 

"ab", "ac", "ad", "abd" => example subsequences for "abcd"
"ba", "abdc" -> not subsequences of "abcd"

value = "abcd"
value[start:end:step] start => inclusive, end => exclusive
"""

# name = "Aravind" 
# #.        2345  
# print(name[2:5:1]) # 2-> 'a', 3 -> 'v', 4 -> 'i' => "avi"

# nums = (3, 4, 5, 8, 9, 10)
# #.      0. 1. 2. 3. 4.  5
# print(nums[1:5:2]) # 1, 3 => (4, 8)
# print(nums[1:100:2]) # 1, 3, 5, 7, 9, ... 99 => (4, 8, 10)

# name = "aravind"
#   {a, r, a, v, i, n, d}
#             -4       -1
# print(name[-1:-4:-2]) # -1, -3 => "di"
# print(name[-1:-4:1]) # -1,0, 1, 2, 3, 4, 5 ...  

# Default values: [start:end:step] => step > 0 => start = 0, end = len(sequence)
# Default values: [start, end, step] => step < 0 => start = -1, end = - len(sequence) - 1
# nums = [4, 5, 9, 10, True]
# print(nums[::2]) # since step is positive: start = 0, end = 5 => nums[0:5:2]
# print(nums[::-2]) # since step is negetive: start = -1, end = -6 => nums[-1:-6:-2] { -1, -3, -5 }

"""
Dictionaries: key, value pair data structure 
- not a sequence , unordered.
"""
# Dictionaries are mutable.
user = { "name":"Aravind", "age": 25, "address": "Waranagal" , "friends": ["Rajesh", "Shruthi"]} # every element in a dictionary should have a key and value
# print(user["name"], user.get("age"))
# user["age"] = 26
# print(user["age"])
# user["cgpa"] = 6.5
# print(user)

# # Duplicates are not allowed.
# user["name"] = "Aravind Samudrala" # 
# print(user)
# for key in user: # ("name", "age", "address")
#     print(key, user.get(key), user[key])

# user["newkey"] = "Some new value" # one way to update
user.setdefault("profession", "SWE")
# print(user)

# Access a value, update a key's value, adding new key value, iteration through dictionary
# print(user)
# deleted_value = user.pop("profession1", "SDE")
# print(deleted_value)
# print(user)

deleted_friend = user.get("friends").pop(0)

print(deleted_friend)
print(user)

# Homework: Solve two sum problem, 3 sum, 4 sum