from numpy import sort


def anagram_king():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    if sorted(s1) == sorted(s2):
        print("Yes")
    else:
        print("No")