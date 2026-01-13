def main():
    if len(integer_list) != n:
        return
    elif len(integer_list) == n:
        t =(i for i in integer_list)
        print(str(hash(t)))
    return

if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    main()