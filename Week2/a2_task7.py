def big_brother_in_shop_list():
    s = input("Write list of your words: ").split(" ")
    # list = [prod for prod in s]
    # unique_dict = {}
    # for prod in list:
    #     if prod not in unique_dict:
    #         unique_dict[prod] = 1
    #     else:
    #         unique_dict[prod] += 1
    
    
    s = input("Write list of your words: ").split(" ")
    # Simpler: use Counter instead of manual dict
    from collections import Counter
    unique_dict = Counter(s)
    
    # 1. Print the entire dict
    print("All items and counts:")
    for item, count in unique_dict.items():
        print(f"  {item}: {count}")
    
    # 2. Most popular item(s)
    max_count = max(unique_dict.values())
    most_popular = [item for item, count in unique_dict.items() if count == max_count]
    print(f"\nMost popular: {most_popular} (count: {max_count})")
    
    # 3. Items purchased once
    # purchased_once = [item for item, count in unique_dict.items() if count == 1]
    print(f"\nPurchased once: {[item for item, count in unique_dict.items() if count == 1]}")
    
    # 4. Sorted by frequency (descending), then alphabetically for ties
    sorted_items = sorted(unique_dict.items(), key=lambda x: (-x[1], x[0]))
    print("\nSorted by frequency:")
    for item, count in sorted_items:
        print(f"  {item}: {count}")