# Code to  get ticket to home
#

import farenheit_from_celsium as temp_converter
import basic_calc

def main():
    choosing = input("""
    Please choose task:
          1. Celsioum to Farenheit
          2. Calculator
          3. Even or Odd
          4. Correct version of is_alive()
          5. Birthday
                         
    Enter your choice: 
    """)


    match choosing:
        case "1":
            print(temp_converter.convert())
        case "2":
            basic_calc.calculator()
        case "3":
            number = int(input("Please provide me only numbers(not strings, I don't wanna debug)"))
            if number % 2 != 0:
                print("Number is odd")
            elif number % 2 == 0:
                print("The number is even")
        case "4":
            print("""The wrong code
                  def is_alive(health):
if:
health < 0
False
else:
return true
                  
                  """)
            print("""my version of code
                  def is_alive(health):
                    if health < 0:
                        print("Dead")
                    else:
                        print("Alive")
                  
                  
                  
                  
                  
                  """)
            def is_alive(health):
                    if health < 0:
                        print("Dead")
                    else:
                        print("Alive")
            status = int(input("Are you alive? Give your answer in numeric form(0 is dead and any number is alive): "))
            is_alive(status)

        case "5":
            print("""IN WHICH MONTH YOU WERE BORN
GIVE ANSWER IN NUMERIC FORM""")
            messages_list = ["White snow fell outside the window", "Birds sang beautiful songs", "The sun shone brighter than ever", "The harvest was incredible"]
            month_num = int(input())
            if month_num == 0 or month_num > 12:
                print("This monthes does not exits")
            elif 1 <= month_num <= 2 or month_num == 12:
                print(f"You were born in {month_num}. {messages_list[0]}")
            elif 3 <= month_num <= 5:
                print(f"You were born in {month_num}. {messages_list[1]}")
            elif 6 <= month_num <= 8:
                print(f"You were born in {month_num}. {messages_list[2]}")
            elif 9 <= month_num <= 11:
                print(f"You were born in {month_num}. {messages_list[3]}")

        case "_":
            print("Please provide me number between 1 - 5")

if __name__ == "__main__":
    main() 