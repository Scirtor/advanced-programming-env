# Assignment 2
# CS-2406 Bekmurat Nurzhan
import a2_task1 as task1
import a2_task2 as task2
import a2_task3 as task3
# import a2_task4 as task4
# import a2_task5 as task5
# import a2_task6 as task6
# import a2_task7 as task7
# import a2_task8 as task8

def main():
    print("Welcome to Assignment 2!")
    print("""Choose which task to run:
          1. Task 1 Archer arrows
          2. Task 2 Cyclic shift of string
          3. Task 3 Kindergarten equation
          4. Task 4 Try to conspect if you can
          5. Task 5 License plate? Vasya
          6. Task 6 Communistic list
          7. Task 7 Big brother in shop list
          8. Task 8 Anagram king
          """)
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            task1.archer_arrows()
        case "2":
            task2.cyclic_shift_of_string()
        case "3":
            task3.kindergarten_equation()
        case "4":
            task4.try_to_conspect_if_you_can()
        case "5":
            task5.license_plate_vasya()
        case "6":
            task6.communistic_list()
        case "7":
            task7.big_brother_in_shop_list()
        case "8":
            task8.anagram_king()


if __name__ == "__main__":
    main()