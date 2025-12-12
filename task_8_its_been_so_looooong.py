def rewrite_in_long():
    sentence = input("Enter a sentence: ")
    num = int(input("Enter a number: "))
    for char in sentence:
        print(char*num, end='\n')
    print()  # For a new line after the output