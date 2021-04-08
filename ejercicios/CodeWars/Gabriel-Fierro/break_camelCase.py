'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example: solution("camelCasing")  ==>  "camel Casing"

https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
'''


def solution(s):
    string = ""

    for x in s:
        if x == x.upper():
            string = string + " "
        string = string + x

    return string
