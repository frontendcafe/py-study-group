'''
Number of Rectangles in a Grid
https://www.codewars.com/kata/556cebcf7c58da564a000045

Given a grid of size m x n, calculate the total number of rectangles 
contained in this rectangle. All integer sizes and positions are counted.
'''

def number_of_rectangles(m, n):
    amount = m * n * (m  + 1) * (n + 1) // 4

    return amount


# Clue to solve it: it is a mathematical formula >.>'
# Solved by Gabriella Martinez. https://github.com/martinezga
    reversed_string = ''

    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]

    return reversed_string