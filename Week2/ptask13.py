def inside_brackets(s):
    start = s.find("(")
    end = s.find(")")
    if start != -1 and end != -1 and start < end:
        return s[start + 1:end]
    return ""
