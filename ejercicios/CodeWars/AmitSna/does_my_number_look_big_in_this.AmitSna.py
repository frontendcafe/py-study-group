narcissistic = lambda value: sum([num**len(str(value)) for num in [int(digit) for digit in str(value)]]) == value

def narcissistic(value):
    return sum([num**len(str(value)) for num in [int(digit) for digit in str(value)]]) == value
