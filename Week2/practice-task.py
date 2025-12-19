import ptask1
import ptask2
# import ptask3
# import ptask4
# import ptask5
# import ptask6
# import ptask7
# import ptask8
# import ptask9
# import ptask10
# import ptask11
# import ptask12
# import ptask13
# import ptask14
# import ptask15

def main():
    choice = input("""Please choose task: 
    1. Russian e counter
    Choice here: """)

    match choice:
        case "1":
            ptask1.ru_e_counter()
        case "2":
            ptask2.replace_colons()
        case _:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()



