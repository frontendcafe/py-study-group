class OperacionMatematica:
	"""Basic Math Operations Class"""
	
	def add(self, a, b):
		"""Adds two numbers"""
		return a + b
	
	def substract(self, a, b):
		"""Substracts two numbers"""
		return a - b
	
	def multiply(self, a, b):
		"""Multiplies two numbers"""
		return a * b
	
	def divide(self, a, b=1):
		"""Divides two numbers"""
		return a / b
	
	def int_divide(self, a, b=1):
		"""Divides two numbers by integer part"""
		return a // b
	
	def modulo(self, a, b):
		"""Modulo of two numbers"""
		return a % b
	
	def power(self, a, b):
		"""Power of a number"""
		return a ** b
	
	def root(self, a, b):
		"""Root of a number"""
		return a ** (1 / b)


#Tests
operator = OperacionMatematica()

print(operator.add(1, 1)) #2
print(operator.substract(2, 1)) #1
print(operator.multiply(2, 1)) #2
print(operator.divide(2, 2)) #1.0
print(operator.int_divide(4, 2)) #2
print(operator.modulo(3, 2)) #1
print(operator.power(2, 1)) #2
print(operator.root(144, 2)) #12.0