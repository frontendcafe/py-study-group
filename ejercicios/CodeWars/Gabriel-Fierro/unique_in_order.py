'''
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

Examples:

unique_in_order('AAAABBBCCDAABBB') ==> ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         ==> ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       ==> [1,2,3]

https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
'''


def unique_in_order(iterable):
    list = []
    acum = ""
    for x in iterable:
        if(x != acum):
            acum = x
            list.append(acum)

    return list
