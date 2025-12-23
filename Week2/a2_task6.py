def communistic_list():
    strs = input("Write list of your words: ").split(" ")
    #looking for the longest
    longest = 0
    for word in strs:
        if len(word) > longest:
            longest = len(word)
        else:
            continue
    
    new_strs = ""
    for word in strs:
        if len(word) < longest:
            word += "_" * (longest - len(word))
            # print(word)
            new_strs += word + " "
        else:
            new_strs += word + " "
            continue
    print(new_strs)
    