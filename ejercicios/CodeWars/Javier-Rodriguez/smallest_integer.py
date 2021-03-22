# Find the smallest integer in the array
# https://www.codewars.com/kata/55a2d7ebe362935a210000b2
# Javier Rodriguez

# Version 1
def find_smallest_int(arr):
    resu = arr[0]
    for i in arr:
        if i < resu:
            resu = i
    return resu