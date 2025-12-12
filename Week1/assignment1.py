# This is the main file for Assignment 1
# Here we will add the necessary code to run the assignment tasks
# 

import task_1_greeting as greeting
import task_2_salary_range as salary_range
import task_3_numbers_play as numbers_play
import task_4_sum_of_nums_in_range as sum_nums
import task_5_number_akinator as number_akinator
import task_6_dumb_calculator as calculator
import task_8_its_been_so_looooong as long_task
import task_9_lucky_ticket as lucky_ticket

def main():
    print("Welcome to Assignment 1!")
    print("""Choose which task to run:
          1. Greeting People
          2. Salary Range Calculation
          3. Real Number Play
          4. Sum of Numbers in Range
          5. Guess the Number
          6. Dumb Calculator
          8. It's Been So Loooong Words
          9. Lucky Ticket
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
        case "5":
            print("Please guess the number, then multiply it by 5, add 8, and multiply the result by 2.")
            number = input("Enter the resulted number from the formula: ")
            try:
                float_number = float(number)
                guessed_number = number_akinator.find_num(float_number)
                print(f"The number you initially thought of is approximately: {guessed_number}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        case "6":
            calculator.calculator()
        case "8":
            long_task.rewrite_in_long()
        case "9":
            Ur_ticket = input("Enter your 6-digit ticket number: ")
            print("Are you lucky?")
            print(lucky_ticket.are_you_lucky(Ur_ticket))
        case _:
            print("Invalid choice. We will exit the program.")

if __name__ == "__main__":
    main()
    # this comment