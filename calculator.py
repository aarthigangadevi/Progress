def calculator():
    print("Simple Calculator")
    result = None
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers.")
        return

    operation = input("Choose operation (+, -, *, /, %, **): ")

    if operation == '+':
        result = n1 + n2
    elif operation == '-':
        result = n1 - n2
    elif operation == '*':
        result = n1 * n2
    elif operation == '%':
        result = n1 % n2 if n2!=0 else "Error: Division by Zero"
    elif operation == '**':
        result = n1**n2
    elif operation == '/':
            result = n1 / n2 if n2!=0 else "Error: Division by Zero"
    else:
        result = "Invalid operation"
    print("Result: ", result)

calculator()
