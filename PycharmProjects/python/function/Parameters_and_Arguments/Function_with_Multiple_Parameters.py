# Define a function that calculates the total cost of items
def total_cost(price, tax_rate, quantity):
    total = price * quantity
    tax = total * tax_rate
    return total + tax


# Call the function with arguments
cost = total_cost(10.0, 0.08, 3)
print("Total cost:", cost)
