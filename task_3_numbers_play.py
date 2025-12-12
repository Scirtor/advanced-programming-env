def real_num_play(float_num):
    if float_num >= 100 or type(float_num) is not float:
        print("Please provide a floating-point number lower than 100.")
        return "Invalid input. Reason given above."
    
    rounded_num = round(float_num, 2)
    if rounded_num < float_num:
        print(f"The number {float_num} rounded to two decimal places is {rounded_num}")

    integer_part = int(float_num)
    fractional_part = float_num - integer_part
    return(round(fractional_part * 100 + integer_part / 100, 2))

    
