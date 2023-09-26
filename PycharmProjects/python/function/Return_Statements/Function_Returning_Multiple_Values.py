# Define a function that returns the sum and product of two numbers
def sum_and_product(x, y):
    total = x + y
    product = x * y
    return total, product


# Call the function and capture the results
addition, multiplication = sum_and_product(3, 4)
print("Sum:", addition)  # Output: Sum: 7
print("Product:", multiplication)  # Output: Product: 12
