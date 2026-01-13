import array


def natural_dividable():
    n = int(input("Enter a number: "))
    result = []
    for num in range(1, n + 1):
            digits = [int(d) for d in str(num)]
            if all(d != 0 and num % d == 0 for d in digits):
                result.append(num)
    print(f"The numbers that are divisible by their digits are: {result}")
    return 


def array_replacement():
    m = int(input("Enter the size of the array: "))
    arr = array.array('i', [])
    for _ in range(m):
        element = int(input("Enter an element: "))
        arr.append(element)
    print(f"The original array is: {arr}")
    arr[0], arr[-1] = arr[-1], arr[0]
    print(f"The array after swapping the first and last elements: {arr}")
    return 