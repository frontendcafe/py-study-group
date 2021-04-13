'''
Does my number look big in this?
https://www.codewars.com/kata/5287e858c6b5a9678200083c

A Narcissistic Number is a positive number which is the sum of its own digits, 
each raised to the power of the number of digits in a given base. In this Kata, 
we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcisstic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

Your code must return true or false depending upon whether the given number is a 
Narcissistic number in base 10.
'''


def narcissistic( value ):
    ''' 
    input: value (required) - Positive number
    output: True  - If the given number is a Narcissistic number
            False - If the given number is NOT a Narcissistic number
    '''
    sum_of_digits = 0
    value_list = list(str(value))
    number_of_digits = len(value_list)

    for i in range(number_of_digits):
        number_str = value_list[i]
        sum_of_digits += int(number_str) ** number_of_digits

    return True if value == sum_of_digits else False


# Solved by Gabriella Martínez. https://github.com/martinezga
