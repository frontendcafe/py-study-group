# Opposite number
# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
# Javier Rodriguez

# Version 1
def validate_pin(pin):
    if (pin.isnumeric()):
        if ((len(pin) == 4) or (len(pin) == 6)):
            return True
    return False