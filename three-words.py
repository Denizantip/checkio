def checkio(words):
    count = 0
    for word in words.split():
        if word.isalpha():
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False