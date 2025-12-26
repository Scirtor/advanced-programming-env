from cmath import sqrt


def area_of_shape():
    type_of_shape = input("Enter the type of shape: ").lower()
    if type_of_shape is "triangle":
        first_edge = int(input("Enter the length of the first edge: "))
        second_edge = int(input("Enter the length of the second edge: "))
        third_edge = int(input("Enter the length of the third edge: "))
        semiper = (first_edge + second_edge + third_edge) / 2
        print(f"The area of the triangle with edges {first_edge}, {second_edge}, and {third_edge} is:{sqrt(semiper * (semiper - first_edge) * (semiper - second_edge) * (semiper - third_edge))}")
    elif type_of_shape is "circle":
        rad = int(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {3.14159 * rad * rad}")  
    elif type_of_shape is "rectangle":
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {length * width}")
    elif type_of_shape is "square":
        side = int(input("Enter the length of the side of the square: "))
        print(f"The area of the square is: {side * side}")
    elif type_of_shape is "parallelogram":
        base = int(input("Enter the base length of the parallelogram: "))
        height = int(input("Enter the height of the parallelogram: "))
        print(f"The area of the parallelogram is: {base * height}")
    else:
        print("Invalid shape type entered.")
    return

def read_numbers(prompt):
    parts = input(prompt).split()
    nums = [int(x) for x in parts[:15]]  # keep at most 15
    if len(parts) > 15:
        print("Only the first 15 numbers were kept.")
    return nums


def sum_and_mean():
    first_arr = read_numbers("Please enter numbers separated by spaces: ")
    second_arr = read_numbers("Please enter more numbers separated by spaces: ")
    third_arr = read_numbers("Please enter even more numbers separated by spaces: ")
    print(f"Sum of the elements of first array is {sum(first_arr)}")
    print(f"Sum of the elements of second array is {sum(second_arr)}")
    print(f"Sum of the elements of third array is {sum(third_arr)}")
    print(f"Mean of the elements of first array is {sum(first_arr) / len(first_arr) if first_arr else "Unknown"}")
    print(f"Mean of the elements of second array is {sum(second_arr) / len(second_arr) if second_arr else "Unknown"}")
    print(f"Mean of the elements of third array is {sum(third_arr) / len(third_arr) if third_arr else "Unknown"}")
    return