from __future__ import generators
import random

class Sweets(object):
	name = ""
	recipe = ""

	def cooking(self):
		print "Cooked " + self.name

	def get_recipe(self):
		return self.recipe

	@staticmethod
	def factory(type):
		if type == "Candy":
			return Candy()
		if type == "Biscuit":
			return Biscuit()
		assert 0, "Not available: " + type

class Candy(Sweets):
	name = "Sweet Candy"
	recipe = "A lot of sugar"

class Biscuit(Sweets):
	name = "Sweet Biscuit"
	recipe = "Flour, sugar"

#tests

def outInfo(object):
	print "%s: %s" % (object.name, object.get_recipe())
	object.cooking()

candy = Sweets.factory("Candy")
outInfo(candy)
#print "%s:(%s)" % (candy.name, candy.__class__.__name__)

biscuit = Sweets.factory("Biscuit")
outInfo(biscuit)
#print "%s:(%s)" % (candy.name, candy.__class__.__name__)

#some = Sweets.factory("Some else")

#more tests

def sweetsGen(n):
	types = Sweets.__subclasses__()
	for i in range(n):
		yield random.choice(types).__name__

sweets = [ Sweets.factory(i) for i in sweetsGen(10)]

for sweet in sweets:
	outInfo(sweet)