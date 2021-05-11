class Inventory:
	def __init__(self, content={}, size=4):
		keys = [x for x in range(size)]
		self.content = dict.fromkeys(keys, None)

	def display_inventory(self):
		for key, value in self.content.items():
			print(key, '::', value)

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
				breaks