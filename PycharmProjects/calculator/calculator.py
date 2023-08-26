import operator
import re

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def calculate(expr):
    try:
        parts = re.split(r'([-+*/])', expr)
        parts = [part.strip() for part in parts]

        while len(parts) > 1:
            for op in operators.keys():
                while op in parts:
                    op_index = parts.index(op)
                    num1 = float(parts[op_index - 1])
                    num2 = float(parts[op_index + 1])
                    operation = operators[op]
                    result = operation(num1, num2)
                    parts[op_index - 1:op_index + 2] = [str(result)]

        return float(parts[0])
    except Exception as e:
        return f"Error: {e}"


while True:
    user_input = input("Enter a mathematical expression (or 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Calculator exiting...")
        break

    result = calculate(user_input)
    print("Result:", result)
