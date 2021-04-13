'''
Number of Rectangles in a Grid
https://www.codewars.com/kata/556cebcf7c58da564a000045

Given a grid of size m x n, calculate the total number of rectangles 
contained in this rectangle. All integer sizes and positions are counted.
'''

def number_of_rectangles(m, n):
    amount = m * n * (m  + 1) * (n + 1) // 4

    return amount


# Clue to solve it: it is a mathematical formula
# Solved by Gabriella Martínez. https://github.com/martinezga
