# Python Data Structures: Lists, Tuples, and Dictionaries

## 1. Lists `[]`

**Definition:** Ordered, mutable collections that allow duplicate elements.

### Operations

- **Adding:** \* `list.append(item)`: Adds to the end.
  - `list.insert(index, item)`: Adds at a specific position.
  - `list.extend([item1, item2])`: Merges another list.
- **Removing:**
  - `list.remove(item)`: Removes the first occurrence of the value.
  - `list.pop(index)`: Removes and returns item at index (default is last).
  - `del list[index]`: Deletes using index.
- **Updating:**
  - `list[index] = new_value`
- **Iterating:**
  ```python
  for item in my_list:
      print(item)
  ```
- **Size:** `len(my_list)`

---

## 2. Tuples `()`

**Definition:** Ordered, **immutable** collections. Great for fixed data (records).

### Operations

- **Adding/Removing/Updating:** **Not possible** directly. You must convert to a list, modify, and convert back if changes are needed.
- **Iterating:**
  ```python
  for item in my_tuple:
      print(item)
  ```
- **Size:** `len(my_tuple)`

---

## 3. Dictionaries `{}`

**Definition:** Collections of **Key-Value** pairs. Designed for high-speed lookups.

### Operations

- **Adding/Updating:**
  - `my_dict["key"] = "value"`
  - `my_dict.update({"key": "new_value"})`
- **Removing:**
  - `del my_dict["key"]`
  - `my_dict.pop("key")`: Removes key and returns its value.
- **Finding Size:** `len(my_dict)` returns the number of key-value pairs.

### Iteration

- **Over Keys:** `for k in my_dict.keys():` (or simply `for k in my_dict:`)
- **Over Values:** `for v in my_dict.values():`
- **Over Both:** `for k, v in my_dict.items():`

### Keys: Data Types & The Hash Method

- **Allowed Key Types:** Keys must be **Immutable** (Hashable).
  - **Valid:** strings, integers, floats, booleans, and tuples (if the tuple contains only immutable objects).
  - **Invalid:** lists, sets, or other dictionaries.
- **How Python Decides (Hashing):**
  - When a key is assigned, Python uses the `hash()` function to turn it into an integer.
  - This integer determines where the value is stored in memory.
  - **Same Key Check:** If two objects are used as keys, Python first checks if their `hash()` values are equal. If they are, it then checks for equality using `==`. Only if both match does Python treat them as the "same key."
