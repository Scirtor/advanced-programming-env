def sum_of_nums(number):
    if number == 1:
        return 1
    elif 1 < number < 10 ** 4:
        return number + sum_of_nums(number - 1)
    else:
        return "Invalid input. Please provide a number between 1 and 10,000."