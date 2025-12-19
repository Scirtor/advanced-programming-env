def replace_a_with_o(s):
    replacements = s.count("a")
    new_s = s.replace("a", "o")
    return new_s, replacements, len(s)
