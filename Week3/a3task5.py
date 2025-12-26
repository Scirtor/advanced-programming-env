def fraction_subtractor():
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1, den1 = map(int, input("Enter numerator and denominator of first fraction: ").split())
    num2, den2 = map(int, input("Enter numerator and denominator of second fraction: ").split())

    result_num = num1 * den2 - num2 * den1
    result_den = den1 * den2

    divisor = gcd(abs(result_num), abs(result_den))
    result_num = result_num // divisor
    result_den = result_den // divisor

    print(f"Result: {result_num}/{result_den}")

    return

def all_divisors():
    num = int(input("Give me the number: "))
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    print(f"All divisors of {num} are: {divisors}")
    return
