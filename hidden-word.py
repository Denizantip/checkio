from itertools import zip_longest

def search(text,word):
    for line_number, line in enumerate(text):
        if word in line:
            start_row = end_row = line_number + 1
            start_col = line.find(word) + 1
            end_col = start_col + len(word) 
            return (start_row, start_col, end_row, end_col)
    else:
        rotated_text = [''.join(line) for line in zip_longest(*text, fillvalue="")]
        (start_row, start_col, end_row, end_col) = search(rotated_text,word)
        return (start_col, start_row, end_col, end_row)

def checkio(text, word):
    normalized_text = [line.replace(' ', '').lower() for line in text.splitlines()]
    return search(normalized_text, word)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]


from itertools import zip_longest

def search(text,word):
    for line_number, line in enumerate(text):
        if word in line:
            start_row = end_row = line_number + 1
            start_col = line.find(word) + 1
            end_col = line.find(word) + len(word)
            return (start_row, start_col, end_row, end_col)
    else:
        rotated_text = [''.join(line) for line in zip_longest(*text, fillvalue="")]
        (start_row, start_col, end_row, end_col) = search(rotated_text,word)
        return (start_col, start_row, end_col, end_row)

def checkio(text, word):
    normalized_text = [line.replace(' ', '').lower() for line in text.splitlines()]
    return search(normalized_text, word)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]