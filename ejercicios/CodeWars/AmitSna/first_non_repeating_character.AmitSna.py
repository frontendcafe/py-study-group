def first_non_repeating_letter(string):
    for char in string:
        if string.lower().count(char.lower()) == 1:
            return char
    return ""
