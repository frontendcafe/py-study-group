class FuncionesMatematicas:
	"""Math Functions Class"""

	def average(self, a):
		"""Average from list"""
		
		if a:
			sum = 0
			for num in a:
				sum += num
			return 0 if sum == 0 else sum / len(a)
		else:
			return a
	
	def maximum(self, a):
		"""Max value from list"""
		#return max(a)
		
		if a:
			max = a[0]
			for num in a:
				if num > max:
					max = num
			return max
		else:
			return a
	
	def minimum(self, a):
		"""Min value from list"""
		#return min(a)
		
		if a:
			min = a[0]
			for num in a:
				if num < min:
					min = num
			return min
		else:
			return a
			
	def summation(self, a):
		"""Return sum from nums in list"""
		#sum(a)
		
		sum = 0
		for num in a:
			sum += num
		return sum
	
	def repeated(self, a):
		"""Show repeated values in list"""
		
		return sorted(set([num for num in a if a.count(num) > 1]))
	
	def unique(self, a):
		"""Show unique values in list"""
		
		return sorted(set([num for num in a if a.count(num) == 1]))
	
	def fibo(self, a):
		"""Calculate Fibonacci Sucession from a given quantity of digits"""
		#return [int((((1 + (5 ** 0.5)) / 2) ** (a - 1) / (5 ** 0.5)) + 0.5), a][a < 2]
		
		if a < 2:
			return a
		return self.fibo(a - 1) + self.fibo(a - 2)
			
#Tests

function = FuncionesMatematicas()

print(function.average([3, 2, 1])) #2.0
print(function.maximum([1, 2, 3])) #3
print(function.minimum([3, 1, 2])) #1
print(function.summation([1, 2, -1])) #2
print(function.repeated([1, 1, 1])) #[1]
print(function.unique([1, 1, 1])) #[]
print(function.fibo(7)) #13
