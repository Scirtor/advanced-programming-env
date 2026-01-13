import string
from collections import Counter




def run():
    try:
        with open("text.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()


        text = "".join(lines).lower()
        translator = str.maketrans("", "", string.punctuation)
        text = text.translate(translator)


        words = text.split()
        word_freq = Counter(words)


        with open("analysis.txt", "w", encoding="utf-8") as out:
            out.write(f"Total lines: {len(lines)}\n")
            out.write(f"Total words: {len(words)}\n")
            out.write("Word frequency:\n")
            for word, count in word_freq.items():
                out.write(f"{word}: {count}\n")     

        print("Analysis saved to analysis.txt")


    except FileNotFoundError:
        print("text.txt not found!")