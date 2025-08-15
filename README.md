Here’s a simple **README.md** for your code:

---

# List Operations in Python

## 📌 Overview

This script demonstrates basic Python list operations, including:

* Creating an empty list
* Adding elements using `append()` and `insert()`
* Extending a list with another list
* Removing elements with `pop()`
* Sorting the list
* Finding the index of a specific element

It serves as a beginner-friendly example for understanding how Python list methods work.

---

## 🛠 Steps Performed in the Script

1. **Create an empty list**

   ```python
   my_list = []
   ```

2. **Append elements**

   ```python
   my_list.append(10)
   my_list.append(20)
   my_list.append(30)
   my_list.append(40)
   ```

3. **Insert an element at a specific position**

   * `15` is inserted at the **second position** (index `1`).

   ```python
   my_list.insert(1, 15)
   ```

4. **Extend the list**

   * Adds multiple elements `[50, 60, 70]` at the end.

   ```python
   my_list.extend([50, 60, 70])
   ```

5. **Remove the last element**

   ```python
   my_list.pop()
   ```

6. **Sort the list in ascending order**

   ```python
   my_list.sort()
   ```

7. **Find the index of an element**

   * Retrieves the index of `30` in the sorted list.

   ```python
   index_of_30 = my_list.index(30)
   print("Index of 30:", index_of_30)
   ```

---

## 💻 Example Output

```
List: [10, 15, 20, 30, 40, 50, 60]
Index of 30: 3
```

---

## 📂 How to Run

1. Save the script as `list_operations.py`.
2. Run in terminal:

   ```bash
   python list_operations.py
   ```

