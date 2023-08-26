numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        break   # Exit the loop when num becomes 3
    if num % 2 == 0:
        continue  # Skip even numbers and move to the next iteration
    print(num)

else:
    print("Loop finished.")
