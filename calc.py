# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation20
if operation == '+':
    result = num1 + num2
    operator_str = "+"
elif operation == '-':
    result = num1 - num2
    operator_str = "-"
elif operation == '*':
    result = num1 * num2
    operator_str = "*"
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
        exit()
    result = num1 / num2
    operator_str = "/"
else:
    print("Invalid operation! Please use +, -, *, or /")
    exit()

# Display the result
print(f"{num1} {operator_str} {num2} = {result}")