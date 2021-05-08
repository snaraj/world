'''
	A 'world' is composed of 0 or many shops, towns, beasts, humans.
'''
from town.town import Town
from industries.retail.shop import Shop as Shop
from humans.roles.warrior import Warrior as Warrior

class World:

	towns = []
	shops = []
	humans = {}
	bestiary = {}

	def __init__(self, name='Unknown'):
		self.name = name

	# Unambigous representation
	def __repr__(self):
		return '(World(%r))' % (self.name)

	# Readable representation
	def __str__(self):
		return f'This is {self.name}'

	# Add all avaliable players in a town.
	def add_town(self, name, population):
		town = Town(name, population)
		towns.append(town)

	def add_shop(self, name, catalog):
		shop = Shop(name, catalog)
		shops.append(shop)

	def add_warrior(self, name, age):
		warrior = Warrior(name, age)
		humans['warriors'] = warrior

	def add_wolf(self, health, dmg):
		wolf = Wolf(health, dmg)
		bestiary['wolfs'] = wolf

	# Getters
	def get_towns(self):
		return self.towns

	def get_shops(self):
		return self.shop

	def get_humans(self):
		return self.humans

	def get_bestiary(self):
		return self.bestiary

world = World('world 1')
world.add_town('town 1', 10)
world.add_shop('shop 1', {'dull sword' : [1, 10]})
world.add_warrior('warrior 1', 25)
world.add_wolf(50, 10)


