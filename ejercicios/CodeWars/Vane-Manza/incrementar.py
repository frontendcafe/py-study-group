# -*- coding: utf-8 -*-


def increment_string(strng):
    new_str = ''
    number1 = '1'
    numeros = '0123456789'
    
    if len(strng) == 0:
        new_str = number1
    
    if len(strng) > 0:
        if strng[-1] in 'abecedario':
            new_str = strng + number1
     
        if strng[-1] in numeros:
            for nletra, letra in enumerate(strng):
                if letra in numeros:
                    pos = nletra     
                    mitad_uno = strng[:pos]  
                    mitad_dos =strng[pos:]
                    incrementado = str(int(mitad_dos)+1)
                    # print(incrementado) 
                    mitad_dos = incrementado.zfill(len(strng)-pos)
                    # print(mitad_uno, '+', mitad_dos)
                    new_str = mitad_uno + mitad_dos
                    break    
        
    print(new_str)
    return new_str

test1 = increment_string('foo001')
test = increment_string("foo") # "foo1"
test = increment_string("foobar001") #"foobar002"
test = increment_string("foobar1") # "foobar2"
test = increment_string("foobar00") # "foobar01"
test = increment_string("foobar99") # "foobar100"
test = increment_string("foobar099") # "foobar100"
test = increment_string("") #"1"