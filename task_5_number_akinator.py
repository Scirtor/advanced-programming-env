def find_num(resulted_number):
    if type(resulted_number) is float:
        reversed_formula = round(resulted_number, 2)
    if type(reversed_formula) is int:
        reversed_formula = (resulted_number/2 - 8) / 5
        return reversed_formula
    else: 
        return "Invalid input. Please provide a valid number."