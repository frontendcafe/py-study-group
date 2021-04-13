'''
Powers of 2
https://www.codewars.com/kata/57a083a57cb1f31db7000028

Complete the function that takes a non-negative integer n as input, and 
returns a list of all the powers of 2 with the exponent ranging from 0 to n (inclusive).
'''


def powers_of_two(n):
    ''' 
    input: n (required) - Non-negative integer
    output: powers_of_two - List of all the powers of 2 with the exponent ranging from 0 to n (inclusive)
    '''
    powers_of_two = []

    if n < 0:
        return 'Error. "n" must be a positive number'
    else:
        for i in range(int(n) + 1):
            powers_of_two.append(2 ** i)
        return powers_of_two


# Solved by Gabriella Martínez. https://github.com/martinezga
