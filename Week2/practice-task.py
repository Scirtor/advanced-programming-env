import ptask1
import ptask2
import ptask3
import ptask4
import ptask5
import ptask6
import ptask7
import ptask8
import ptask9
import ptask10
import ptask11
import ptask12
import ptask13
import ptask14
import ptask15

def main():
    choice = input("""Please choose task: 
    1. Russian e counter
    2. Replace colons
    3. Remove dots
    4. Replace a with o
    5. To lowercase
    6. Remove a
    7. Replace n first half
    8. Count words
    9. Word count
    10. Capitalize words
    11. Longest n and replace exclamations
    12. Words ending with I
    13. Inside brackets
    14. Words a or i
    15. Count t
    Choice here: """)
    

    match choice:
        case "1":
            ptask1.ru_e_counter()
        case "2":
            string = input("Please enter text: ")
            print(f"Replaced colons: {ptask2.replace_colons(string)}")
        case "3":
            string = input("Please enter text: ")
            print(f"Removed dots: {ptask3.remove_dots(string)}")
        case "4":
            string = input("Please enter text: ")
            print(f"Replaced a with o: {ptask4.replace_a_with_o(string)}")
        case "5":
            string = input("Please enter text: ")
            print(f"To lowercase: {ptask5.to_lowercase(string)}")
        case "6":
            string = input("Please enter text: ")
            print(f"Removed a: {ptask6.remove_a(string)}")
        case "7":
            string = input("Please enter text: ")
            print(f"Replaced n first half: {ptask7.replace_n_first_half(string)}")
        case "8":
            string = input("Please enter text: ")
            print(f"Count words: {ptask8.count_words(string)}")
        case "9":
            string = input("Please enter text: ")
            word = input("Please enter word: ")
            print(f"Word count: {ptask9.word_count(string, word)}")
        case "10":
            string = input("Please enter text: ")
            print(f"Capitalized words: {ptask10.capitalize_words(string)}")
        case "11":
            string = input("Please enter text: ")
            print(f"Longest n and replace exclamations: {ptask11.longest_n_and_replace_exclamations(string)}")
        case "12":
            string = input("Please enter text: ")
            print(f"Words ending with I: {ptask12.words_ending_with_I(string)}")
        case "13":
            string = input("Please enter text: ")
            print(f"Inside brackets: {ptask13.inside_brackets(string)}")
        case "14":
            string = input("Please enter text: ")
            print(f"Words a or i: {ptask14.words_a_or_i(string)}")
        case "15":
            string = input("Please enter text: ")
            print(f"Count t: {ptask15.count_t(string)}")    
        case _:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()



