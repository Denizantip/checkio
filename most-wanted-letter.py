from string import ascii_lowercase
 
def checkio(text):
    letters = [x for x in text.lower() if x in ascii_lowercase]
    counts = sorted({x : letters.count(x) for x in letters}.items(), key=lambda x:x[1], reverse=True)
    wanted_count = counts[0][1]
    wanted = sorted([x[0] for x in counts if x[1] == wanted_count])[0]
    return wanted

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
