def longest_n_and_replace_exclamations(s):
    max_n = current = 0
    for ch in s:
        if ch == "n":
            current += 1
            max_n = max(max_n, current)
        else:
            current = 0
    return s.replace("!", "."), max_n
