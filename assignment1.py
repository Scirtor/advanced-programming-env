# This is the main file for Assignment 1
# Here we will add the necessary code to run the assignment tasks
# 

import task_1_greeting as greeting
import task_2_salary_range as salary_range


def main():
    print("Welcome to Assignment 1!")
    print("""Choose which task to run:
          1. Greeting People
          2. Salary Range Calculation
          
          """)
    choice = input("Enter here:")
    match choice:
        case "1":
            greeting.greeting_people()
        case "2":
            numbers = input("Enter a list of numbers separated by spaces(If You need sample result just leave empty): ")
            number_list = list(map(int, numbers.split()))
            result = salary_range.range(number_list)
            print(f"The salary range is: {result}")
        case _:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
    