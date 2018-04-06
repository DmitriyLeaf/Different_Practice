# coding: utf-8

'''
#Base classes exempl, but we we don’t need them

class Obstacle:
	def action(self):
		raise NotImplementedError()

class Character:
	def interact_with(self, obstacle):
		raise NotImplementedError()

#Perhaps we cen “tagging classes” like this:

class Obstacle: 
	pass

class Character: 
	pass

class GameElementFactory: 
	pass
'''


class Bird: #(Character):
	def interact_with(self, obstacle):
		print "Bird has encountered a", obstacle.action()

class Human: #(Character):
	def interact_with(self, obstacle):
		print "Human now works a", obstacle.action()

class Tree: #(Obstacle):
	def action(self):
		print "Tree"

class Pencil: #(Obstacle):
	def action(self):
		print "Pencil"

'''
#Abstract Factory
class WorldElementFactory:
	def make_character(self):
		raise NotImplementedError()

	def make_obstacle(self):
		raise NotImplementedError()
'''

#Concrete factories
class BirdAndTree: #(WorldElementFactory):
	def make_character(self):
		return Bird()

	def make_obstacle(self):
		return Tree()

class HumanAndPencil: #(WorldElementFactory):
	def make_character(self):
		return Human()

	def make_obstacle(self):
		return Pencil()

class WorldEnvironment:
	def __init__(self, factory):
		self.factory = factory
		self.character = factory.make_character()
		self.obstacle = factory.make_obstacle()

	def live(self):
		self.character.interact_with(self.obstacle)

world_first = WorldEnvironment(BirdAndTree())
world_second = WorldEnvironment(HumanAndPencil())

world_first.live()
world_second.live()