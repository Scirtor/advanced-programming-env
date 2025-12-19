def replace_n_first_half(s):
    half = len(s) // 2
    first = s[:half].replace("n", "*")
    return first + s[half:]
