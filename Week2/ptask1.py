def ru_e_counter():
    string = input("Please enter Russian text: ")
    count = 0
    string = string.split(" ")
    for word in string:
        if word.capitalize()[0] == "Е":
            count += 1
            print(word)
    print(f"The number of words starting with 'е' is {count}")

