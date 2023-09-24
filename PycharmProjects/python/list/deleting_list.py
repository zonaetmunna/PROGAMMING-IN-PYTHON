fruits = ["apple", "banana", "orange", "jam"]

# Delete the first element (index 0) from the list
del fruits[0]
print(fruits)

# Remove the first occurrence of "banana" from the list
fruits.remove("banana")
print(fruits)

# Remove the second element (index 1) from the list
fruits.pop(1)
print(fruits)

numbers = [1, 2, 3, 4, 5]

# Remove elements from index 1 to index 3
numbers[1:4] = []
print(numbers) 

