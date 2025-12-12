def range(list_of_numbers):
    
    if not list_of_numbers:
        list_of_numbers = [100, 200, 1000]
        print("No input provided. Using sample data: [100, 200, 1000]")
        print("Calculating salary range...")
        return (max(list_of_numbers) - min(list_of_numbers))
    print(list_of_numbers)
    print("Calculating salary range...")
    return (max(list_of_numbers) - min(list_of_numbers))
