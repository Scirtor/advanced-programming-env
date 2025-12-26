from time import sleep as sl
from math import sqrt


def triangle_area(first_edge, second_edge, third_edge):
    """Return area of triangle via Heron's formula."""
    semiperimeter = (first_edge + second_edge + third_edge) / 2
    return sqrt(
        semiperimeter
        * (semiperimeter - first_edge)
        * (semiperimeter - second_edge)
        * (semiperimeter - third_edge)
    )

def bestagons():
    print("""The bestagons are HEXAGOOONS
OK, enough joking
""")
    edge_len = int(input("Enter the length of the edge: "))
    print("Thinking...")
    sl(1)
    single_tri_area = triangle_area(edge_len, edge_len, edge_len)
    print("The area of your hexagon is:", single_tri_area * 6)
    return

def area_of_triangle():
    print("Ok, rectangles. Give me two sides of three rectangles.")
    rect1_width, rect1_height = map(int, input("Write the width and height of the first rectangle separated by a space: ").split(" "))
    rect2_width, rect2_height = map(int, input("Write the width and height of the second rectangle separated by a space: ").split(" "))
    rect3_width, rect3_height = map(int, input("Write the width and height of the third rectangle separated by a space: ").split(" "))
    print(f"The area of the first rectangle is {rect1_width * rect1_height}")
    print(f"The area of the second rectangle is {rect2_width * rect2_height}")
    print(f"The area of the third rectangle is {rect3_width * rect3_height}")
    return