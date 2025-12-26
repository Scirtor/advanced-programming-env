def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def fraction_dividor():
    a, b = map(int, input("Enter numerator and denominator of first fraction: ").split())
    c, d = map(int, input("Enter numerator and denominator of second fraction: ").split())

    numerator = a * d
    denominator = b * c
    
    common_divisor = gcd(numerator, denominator)
    
    numerator = numerator // common_divisor
    denominator = denominator // common_divisor
    print(f"The result of division is {numerator}/{denominator}")
    return 



def is_point_inside_circle(p_x, p_y, center_a, center_b, radius):
    
    distance_squared = (p_x - center_a) ** 2 + (p_y - center_b) ** 2
    return distance_squared < radius ** 2


def points_in_circle():
    center_a, center_b = map(int, input("Enter center coordinates of the circle: ").split())
    radius = int(input("Enter radius of the circle: "))
    count = 0
    n = int(input("Enter number of points: "))
    points = []
    for _ in range(n):
        x, y = map(int, input("Enter point coordinates (x y): ").split())
        points.append((x, y))
        print(points)
    inside_points = []
    
    for point in points:
        if is_point_inside_circle(point[0], point[1], center_a, center_b, radius):
            count += 1
            inside_points.append(point)
    
    print(f"Number of points inside circle: {count}")
    print(f"Points inside: {inside_points}")
    return count