def kindergarten_equation():
    equation = input("Write the equation(ex. x+1=2): ")

    if '=' not in equation:
        print("Invalid equation format")
        return
        
    left, right = equation.split('=')
    # print("left:", left)
    # print("right:", right)
    
    # try: # this code is not understandable, so I'll write my own
    #     for x_val in range(-10, 10):
    #             if eval(left.replace('x', str(x_val))) == eval(right.replace('x', str(x_val))):
    #                 print(f"x = {x_val}")
    #                 return:
    #     print("No solution found")
    # except:
    #         print("Error evaluating equation")


    if left[2] == "x":
        if left[1] == "-":
            print(int(left[0]) - int(right))
        elif left[1] == "+":
            print(int(right) - int(left[0]))
        else: print("Error: Couldn't parse the equation")
    else: # case left[0] == "x"
        if left[1] == "-":
            print(int(left[0]) + int(right))
        elif left[1] == "+":
            print(int(right) - int(left[0]))
        else: print("Error: Couldn't parse the equation")
