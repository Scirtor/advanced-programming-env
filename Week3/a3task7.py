def xyzt():
    sides = list(map(float, input("Enter 4 sides (a, b, c, d): ").split()))
    diagonal = float(input("Enter diagonal: "))

    x, y, z, t = sides
    diag = diagonal

    area1 = 0.5 * x * y
    
    s2 = (z + t + diag) / 2
    area2 = (s2 * (s2 - z) * (s2 - t) * (s2 - diag)) ** 0.5
    
    total_area = area1 + area2
    print(f'Area of quadrilateral: {total_area}')
    return

def integer_to_octal():
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    octal_code = format(n, '010o')
    print(octal_code)
    return 
