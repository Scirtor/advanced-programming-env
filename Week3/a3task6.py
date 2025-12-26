def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

def lcm(a, b):
    return a * b // gcd(a, b)

def gdc_and_lcm():
    a, b = map(int, input("Enter two natural numbers: ").split())
    print(f'GCD: {gcd(a, b)}, LCM: {lcm(a, b)}')
    return

def area_of_quadrilateral():
    sides = list(map(float, input("Enter 4 sides (a, b, c, d): ").split()))
    diagonal = float(input("Enter diagonal: "))

    a, b, c, d = sides
    diag = diagonal

    s1 = (a + b + diag) / 2 
    s2 = (c + d + diag) / 2

    area1 = (s1 * (s1 - a) * (s1 - b) * (s1 - diag)) ** 0.5 #Bretschnider
    area2 = (s2 * (s2 - c) * (s2 - d) * (s2 - diag)) ** 0.5

    total_area = area1 + area2
    print(f'Area of quadrilateral: {total_area}')
    return
