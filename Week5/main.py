import task1
import task2
import task3
import task4
import task5




def main():
    while True:
        print("\n=== Assignment 5 Menu ===")
        print("1. Task 1 – Text File Analysis")
        print("2. Task 2 – JSON Student Average")
        print("3. Task 3 – Person / Student OOP")
        print("4. Task 4 – Employee / Manager OOP")
        print("5. Task 5 – Bank Account")
        print("0. Exit")


        choice = input("Select task: ")

        match choice:
            case "1":
                task1.run()
            case "2":
                task2.run()
            case "3":
                task3.run()
            case "4":
                task4.run()
            case "5":
                task5.run()
            case "0":
                print("Goodbye!")
                break
            case _:
                print("Invalid option!")    



if __name__ == "__main__":
    main()