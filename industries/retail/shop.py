'''
	Blueprint for a shop
'''
class Shop:

	def __init__(self, name, inventory):
		self.name = name
		self.inventory = inventory

	def __str__(self):
		format_dictionary = {'name' : self.name, 'inventory' : self.inventory}
		return 'Shop: {name} \n Inventory: {inventory}'.format(**format_dictionary)

	def get_inventory(self):
		return self.inventory

	def get_shop_name(self):
		return self.name

shop = Shop('ice cream wonderland', {'chocolate' : 10, 'vanilla' : 12})





