def words_a_or_i(s):
    return [w for w in s.split() if w.startswith("a") or w.endswith("i")]
