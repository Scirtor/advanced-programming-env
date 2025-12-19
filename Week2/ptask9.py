def word_count(text, word):
    text = text.lower()
    word = word.lower()
    return text.split().count(word)

