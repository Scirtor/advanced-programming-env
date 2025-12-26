
def natural_dividable():
    n = int(input("Enter a number: "))
    result = []
    for num in range(1, n + 1):
            digits = [int(d) for d in str(num)]
            if all(d != 0 and num % d == 0 for d in digits):
                result.append(num)
    print(f"The numbers that are divisible by their digits are: {result}")
    return 


def array_repplacement():
    
    return