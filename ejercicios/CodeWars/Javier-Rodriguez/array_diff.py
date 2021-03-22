# Array.diff
# https://www.codewars.com/kata/523f5d21c841566fde000009
# Javier Rodriguez

# Version 1
def array_diff(a, b):
    diff = []
    if (len(a) == 0):
        return diff
    if (len(b) == 0):
        return a
    for e in a:
        if not (e in b):
            diff.append(e)
    return diff