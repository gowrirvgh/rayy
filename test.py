# Define a function for the calculator
def calculator():
    print("Simple Python Calculator")
    
    # Ask the user for the operation they want to perform
    operation = input("Choose operation (+, -, *, /): ")

    # Ask the user for two numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers.")
        return

    # Perform the chosen operation
    if operation == '+':
        print(f"The result is: {num1 + num2}")
    elif operation == '-':
        print(f"The result is: {num1 - num2}")
    elif operation == '*':
        print(f"The result is: {num1 * num2}")
    elif operation == '/':
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            print(f"The result is: {num1 / num2}")
    else:
        print("Invalid operation!")

# Run the calculator
calculator()

