class Testing:
	def __init__(self, init_value):
		if type(init_value) != int:
			raise TypeError
		if init_value % 2 == 1:
			raise ValueError
		else:
			self.value = init_value

try:
	test1 = Testing(5)
except ValueError:
	print("Odd")
except TypeError:
	print("Wrong type")

try:
	test2 = Testing(2.5)
except ValueError:
	print("Odd")
except TypeError:
	print("Wrong type")
