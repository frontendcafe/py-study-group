'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example: solution("camelCasing")  ==>  "camel Casing"

https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
'''


def solution(s):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    string = ""

    for x in s:
        if(x in letters):
            string = string + " "
        string = string + x

    return string
