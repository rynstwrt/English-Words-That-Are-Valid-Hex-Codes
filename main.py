from english_words import get_english_words_set
import re


words = get_english_words_set(["web2", "gcide"], lower=True)
pattern = re.compile(r"[a-fA-F0-9]{6}")


for word in words:
    if len(word) == 6 and pattern.match(word):
        print(word)