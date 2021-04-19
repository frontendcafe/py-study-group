'''
Will you make it?
https://www.codewars.com/kata/5861d28f124b35723e00005e
'''


def zero_fuel(distance_to_pump, mpg, fuel_left):
    '''
    input: distance_to_pump (required) - Nearest distance to pump in miles
           mpg (required) - Miles per gallon
           fuel_left (required) - Gallons left
    output: True - It is possible to get to the pump
            False - It is NOT possible to get to the pump
    '''
    gallons_needed = distance_to_pump / mpg
    return True if gallons_needed <= fuel_left else False


# Solved by Gabriella Martínez. https://github.com/martinezga