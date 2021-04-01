'''
String repeat 
https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python
'''
def repeat_str(repeat, string):
    str = ""
    for x in range(0, repeat):
        str = str + string

    return str