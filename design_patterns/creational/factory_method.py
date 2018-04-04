class Sweets(object):
	def cooking(self):
		raise NotImplementedError()

	def taste(self):
		raise NotImplementedError()

	@staticmethod
	def factory(type):
		if type == "Candy":
			return Candy()
		if type == "Biscuit":
			return Biscuit()
		assert 0, "Not available:" + type

class Candy(Sweets):

class Biscuit(Sweets):

def sweetsGen(n):