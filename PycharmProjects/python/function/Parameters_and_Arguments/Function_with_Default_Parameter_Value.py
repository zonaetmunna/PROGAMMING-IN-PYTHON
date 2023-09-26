# Define a function to calculate the area of a rectangle with a default width
def rectangle_area(length, width=2.0):
    area = length * width
    return area


# Call the function without specifying the width
area1 = rectangle_area(5)  # Default width of 2.0 is used
print("Area 1:", area1)

# Call the function with a specific width
area2 = rectangle_area(5, 3)  # Width of 3.0 is provided
print("Area 2:", area2)
