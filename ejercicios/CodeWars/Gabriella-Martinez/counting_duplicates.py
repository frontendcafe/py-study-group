'''
Count the number of Duplicates
https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
'''


def duplicate_count(text):
    '''
    input: text (required) - Alphabetic characters and numeric digits
    output: char_duplicate_num - Number of times a digit occurs more than once
    '''
    letters_count = {}
    char_duplicate_num = 0
    text = text.lower()

    for letter in text:
        letters_count.setdefault(letter, text.count(letter))
    for value in letters_count.values():
        if value >= 2:
            char_duplicate_num += 1

    return char_duplicate_num


# Solved by Gabriella Martínez. https://github.com/martinezga