# Basic Calculator Program
def calculator():
    print("Welcome to the Basic Calculator!")

    # Input two numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # Input the mathematical operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the operation and display the result
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter +, -, *, or /.")

# Run the calculator
calculator()
