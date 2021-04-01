'''
Vowel count
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

https://www.codewars.com/kata/54ff3102c1bad923760001f3
'''
def get_count(input_str):
    num_vowels = 0
    # your code here
    for x in input_str:
        result = isAVowel(x)
        if(result):
            num_vowels += 1 
    return num_vowels

def isAVowel(character):
    
    if character == 'a':
        return True
    if character == 'e':
        return True
    if character == 'i':
        return True
    if character == 'o':
        return True
    if character == 'u':
        return True