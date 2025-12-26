def right_triangles():
    try:
        leg1, leg2 = map(int, input("Enter the lengths of the two legs separated by a space: ").split())
        leg3, leg4 = map(int, input("Enter the lengths of another two legs separated by a space: ").split())
        
        if leg1 <= 0 or leg2 <= 0 or leg3 <= 0 or leg4 <= 0:
            print("Error: All leg lengths must be positive numbers.")
            return
        
        hypo1 = (leg1 ** 2 + leg2 ** 2) ** 0.5
        hypo2 = (leg3 ** 2 + leg4 ** 2) ** 0.5
        print(f"The hypotenuse of the first right triangle is {hypo1}")
        print(f"The hypotenuse of the second right triangle is {hypo2}")
        print(f"The larger hypotenuse is {max(hypo1, hypo2)}")
        print(f"The smaller hypotenuse is {min(hypo1, hypo2)}")
    except ValueError:
        print("Error: Please enter valid integers separated by spaces.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return

def alphabetically_correct():
    s = input("Enter a string: ").split()
    s = [word.lower() for word in s]
    new_s = ""
    for word in s:
        word = sorted(word)
        # print(sorted(word))
        word = "".join(word)
        new_s += " " +word
        # print(word)
    print(new_s)

    return