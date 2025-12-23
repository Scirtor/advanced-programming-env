def try_to_conspect_if_you_can():
    n, m = map(int, input("Write your n and m vars: ").split(" "))
    s = input("Write your string s: ")
    if len(s) > n:
        raise ValueError("Input too long")
    if m < 0 or m > len(s):
        print(0)
        return
    uniques = [s[i:i+m] for i in range(len(s) - m + 1)]
    print(len(uniques))