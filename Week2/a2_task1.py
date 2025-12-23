def archer_arrows():
    s =  input(f"Write your arrows if you want to count into one line like this \n >>--> or <--<< or whatever combination of '<>-': \n")
    
    counter = 0    

    for char in range(len(s)):
        if s[char:char+5] == "<--<<" or s[char:char+5] == ">>-->":
            counter += 1
            print("+")
        else:
            continue

    print(counter)
    