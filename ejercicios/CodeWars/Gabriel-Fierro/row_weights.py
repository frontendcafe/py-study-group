''' 
Task: Given an array of positive integers (the weights of the people), return a new array/tuple
of two integers, where the first one is the total weight of team 1, and the second one is the 
total weight of team 2.

https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9
'''

def row_weights(array):
    i = 0
    longitud = 0
    longitud = len(array)
    even = 0
    odd = 0
    
    while(i < longitud):
        if(i % 2 == 0):
            even += array[i]
        else:
            odd += array[i]
        i += 1
            
    return (even, odd)