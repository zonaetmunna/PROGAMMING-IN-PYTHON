# Define a function to calculate the area of a rectangle
def rectangle_area(length, width):
    area = length * width
    return area


# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Call the function and print the result
area = rectangle_area(length, width)
print("Area of the rectangle:", area)
