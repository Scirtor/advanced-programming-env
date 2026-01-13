
def lim_n(n):
    if n < 2 or n > 10:
        # print("Length of n is 1 or higher than 10")
        exit()

def check_arr(array_elem):
    if array_elem < -100 or array_elem > 100:
        # print("One element is bigger than 100 or less than -100")
        exit()

def main(n, arr):
    # print(max(arr))
    lim_n(n)

    max_arr = max(arr)
    second_max = 0
    if len(arr) != n:
        # print("Wrong array size")
        return
    for i in arr:
        check_arr(i)
        if i < max_arr and i > second_max:
            second_max = i
            # print(second_max)
        else:
            continue
    print(second_max) 
    return 


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    main(n, arr)