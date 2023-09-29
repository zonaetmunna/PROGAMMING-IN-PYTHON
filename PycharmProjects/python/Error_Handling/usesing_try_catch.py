try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ArithmeticError:
    print("An arithmetic error occurred.")

