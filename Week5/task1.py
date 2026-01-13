import string
from collections import Counter
import os


def run():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "text.txt")
        with open(file_path , "r", encoding="utf-8") as file:
            lines = file.readlines()


        text = "".join(lines).lower()
        translator = str.maketrans("", "", string.punctuation)
        text = text.translate(translator)


        words = text.split()
        word_freq = Counter(words)


        with open("./Week5/analysis.txt", "w", encoding="utf-8") as out:
            out.write(f"Total lines: {len(lines)}\n")
            out.write(f"Total words: {len(words)}\n")
            out.write("Word frequency:\n")
            for word, count in word_freq.items():
                out.write(f"{word}: {count}\n")     

        print("Analysis saved to analysis.txt")


    except FileNotFoundError:
        print("text.txt not found!")