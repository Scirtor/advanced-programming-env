# This is the main file for Assignment 1
# Here we will add the necessary code to run the assignment tasks
# 

import task_1_greeting as greeting
import task_2_salary_range as salary_range
import task_3_numbers_play as numbers_play
import task_4_sum_of_nums_in_range as sum_nums

def main():
    print("Welcome to Assignment 1!")
    print("""Choose which task to run:
          1. Greeting People
          2. Salary Range Calculation
          3. Real Number Play
          4. Sum of Numbers in Range
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
        case "3":
            number = input("Enter a floating-point number lower than 100: ")
            try:
                float_number = float(number)
                print("Float number received: ", float_number)
                print("If we try to round it to two decimal places and compare with the original number...")
                print(f"We will get {numbers_play.real_num_play(float_number)}")
            except ValueError:
                print("Invalid input. Please enter a valid floating-point number.")
        case "4":
            number = input("Enter a number between 1 and 10,000: ")
            int_number = int(number)
            result = sum_nums.sum_of_nums(int_number)
            print(f"The sum of numbers from 1 to {int_number} is: {result}")
        case _:
            print("Invalid choice. We will exit the program.")

if __name__ == "__main__":
    main()
    