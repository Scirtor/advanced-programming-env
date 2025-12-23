def cyclic_shift_of_string():
    a = input("Write the main string: ").strip()
    b = input("Write the string to shift: ").strip()
    
    cyclic_shifts = set()
    for i in range(len(b)):
        cyclic_shift = b[i:] + b[:i]
        cyclic_shifts.add(cyclic_shift)
    
    count = 0
    b_len = len(b)
    
    for i in range(len(a) - b_len + 1):
        substring = a[i:i + b_len]
        if substring in cyclic_shifts:
            count += 1
    
    print(count)


if __name__ == "__main__":
    cyclic_shift_of_string()