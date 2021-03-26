def persistence(n):
    counter = 0
    while n > 9:
        accumulator = 1
        for digit in [int(digit) for digit in str(n)]:
            accumulator *= digit
        counter += 1
        n = accumulator
    return counter
