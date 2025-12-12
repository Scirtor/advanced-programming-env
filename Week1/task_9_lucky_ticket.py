def are_you_lucky(ticket_number):
    if len(ticket_number) != 6 or not ticket_number.isdigit():
        return "Invalid input. Please provide a 6-digit ticket number."
    
    first_half = ticket_number[:3]
    second_half = ticket_number[3:]
    
    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)
    
    if sum_first_half == sum_second_half:
        return "You have a lucky ticket!"
    else:
        return "Unfortunately, your ticket is not lucky."