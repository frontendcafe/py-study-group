validate_pin = lambda pin: pin.isnumeric() and len(pin) in (4, 6)

def validate_pin(pin):
  return pin.isnumeric() and len(pin) in (4, 6)
