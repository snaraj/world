'''
	A 'world' is composed of 0 or many shops, towns, beasts, humans.
'''
from humans.roles.warrior.warrior import Warrior
from town.town import Town
from industries.retail.shop import Shop
from bestiary.wolf import Wolf

class World:

	# Every world gets initialized with an empty list/directory of towns, shops, humans, beasts. (entities)
	def __init__(self, name='Unknown'):
		self.name = name
		self.towns = []
		self.shops = []
		self.humans = {}
		self.bestiary = {}

	# Unambigous representation
	def __repr__(self):
		return '(World(%r))' % (self.name)

	# Readable representation
	def __str__(self):
		return f'This is {self.name}'

	# Add all avaliable entities in a town.
	def add_town(self, name, population):
		town = Town(name, population)
		self.towns.append(town)

	def add_shop(self, name, catalog):
		shop = Shop(name, catalog)
		self.shops.append(shop)

	def add_warrior(self, name, age):
		warrior = Warrior(name, age)
		self.humans['warriors'] = warrior

	def add_wolf(self, health, dmg):
		wolf = Wolf(health, dmg)
		self.bestiary['wolfs'] = wolf

	# Getters
	def get_towns(self):
		return self.towns

	def get_shops(self):
		return self.shop

	def get_humans(self):
		return self.humans

	def get_bestiary(self):
		return self.bestiary

	def display_world(self):
		return f'{self.name}: \n towns: {self.towns} shops: {self.shops} humans: {self.humans} bestiary: {self.bestiary}'

def main():
	
	world = World('world 1')
	world.add_town('town 1', 10)
	world.add_shop('shop 1', {'dull sword' : [1, 10]})
	world.add_warrior('warrior 1', 25)
	world.add_wolf(50, 10)

	print(world.display_world())

if __name__ == "__main__":
    main ()