''' 
Mumbling

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
'''

def accum(s):
    # Defino variables con valores iniciales
    position = 0
    longitud = 0
    longitud = len(s)
    i = 0
    string = ""
    
    while(i < longitud):
        # El primer character está capitalizado
        if(i == 0):
            string = string + s[i] + "-"
        else:
            string += s[i].capitalize() + (s[i] * position).lower() + "-"  
        i += 1
        position += 1
        
    return string[:-1]
