from humans.human import Human
from humans.inventory.inventory import Inventory

class Warrior(Human):
	
	# Inherits from human.
	def __init__(self, name='unknown warrior', age='unknown age'):
		# Inherits human attributes as well as the human_attribute_tree.
		super().__init__()
		# Adding the attribute value 'combat abilities' to the human_attribute_tree.
		self.warrior_attribute_tree = self.human_attribute_tree | {'combat abilities' : 5}
		# Normal warrior/human atttributes, maybe put this in Human?
		self.name = name
		self.age = age
	
	# Updated print method.	
	def __str__(self):
		return f'id: {self.human_identifier} \n \
		NAME: {self.name} ; AGE: {self.age} ; COINS: ${self.coins} \n \
		attributes: {self.warrior_attribute_tree} \n \
		inventory: {self.inventory}'

	# Implementing abstract methods from Human.
	def get_age(self):
		return self.age

	def get_name(self):
		return self.name

	''' 
	Takes in an inventory with default entries, adds items until there are no more default
	slots open (default are treated as empty spaces). 
	'''
	def add_to_inventory(self, item : str, amount : int):
		for key, value in self.inventory.items():
			if value == None:
				del self.inventory[key]
				self.inventory[item] = amount
				break
			else:
				return 'Inventory is Full.'
				break



warrior = Warrior()
warrior.add_to_inventory('sword', 1)
warrior.add_to_inventory('shield', 1)
warrior.add_to_inventory('helm', 1)
warrior.add_to_inventory('bow', 1)
warrior.add_to_inventory('dagger', 1)

# warrior.inventory['sword'] = 1
print(warrior)
