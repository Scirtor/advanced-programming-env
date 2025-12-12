def calculator():
    First_number = input("Enter the first number: ")
    
    Second_number = input("Enter the second number: ")
    try:
        First_number = float(First_number)
        Second_number = float(Second_number)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    Operation = input("Enter the operation (+, -, *, /): ")
    print(First_number)
    if First_number.is_integer():
        First_number = int(First_number)
    if Second_number.is_integer():
        Second_number = int(Second_number)

    if Operation == "+":
        Result = First_number + Second_number
        print(f"The result of {First_number} + {Second_number} is {Result}")
    elif Operation == "-":
        Result = First_number - Second_number
        print(f"The result of {First_number} - {Second_number} is {Result}")
    elif Operation == "*":
        Result = First_number * Second_number
        print(f"The result of {First_number} * {Second_number} is {Result}")
    elif Operation == "/":
        if Second_number != 0:
            Result = First_number / Second_number
            print(f"The result of {First_number} / {Second_number} is {Result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")