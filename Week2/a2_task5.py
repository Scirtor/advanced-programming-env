def license_plate_vasya():
    licenses_num = int(input("How many licenses Vasya remember: "))
    licenses = [
                ]
    for _ in range(licenses_num):
        licenses.append(input("Enter license plate: ").upper())
    
    for i in range(licenses_num):
        letters_in = 0
        digits = 0
        # chtck for a license
        for ch in licenses[i]:
            if ch.isalpha():
                letters_in += 1
            elif ch.isdigit():
                digits += 1
            
            
        
        if letters_in != 3 or digits != 3:
                # print(f"Incorrect license plate format: {licenses[i]}")
                print(licenses[i] +"   |  No")
                continue


        allowed = 0
        for ch in licenses[i]:
            if ch in "ABCEHKMOPTX":
                # print(f"There is allowed character")
                allowed += 1
            else:
                continue
        if allowed > 3 or allowed < 3:
            print(licenses[i] +"   |  No")
        else:
            print(licenses[i] +"   |  Yes")
            