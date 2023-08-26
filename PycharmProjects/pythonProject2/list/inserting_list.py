fruits = ["apple", "banana", "orange"]

# Insert "grape" at index 1
fruits.insert(1, "grape")
print(fruits)

fruits = ["apple", "banana", "orange"]
additional_fruits = ["grape", "kiwi"]

# Extend the list with elements from additional_fruits
fruits.extend(additional_fruits)
print(fruits)  # Output: ["apple", "banana", "orange", "grape", "kiwi"]

fruits = ["apple", "banana", "orange"]
additional_fruits = ["grape", "kiwi"]

# Concatenate the lists
combined_fruits = fruits + additional_fruits
print(combined_fruits)  # Output: ["apple", "banana", "orange", "grape", "kiwi"]


