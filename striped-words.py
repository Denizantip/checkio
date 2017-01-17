from string import punctuation, digits
import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):
    result = ''
    count = 0
    for word in text.translate(str.maketrans(punctuation, ' '*len(punctuation))).split():
        if len(word) > 1 and all(char not in digits for char in word):
            for ch in word:
                if ch.upper() in VOWELS:
                    result += '0'
                elif ch.upper() in CONSONANTS:
                    result += '1'
            if len(re.findall(r'00|11', result)) == 0:
                count += 1
            result = ''
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
