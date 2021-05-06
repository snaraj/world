'''
	Blueprint for a shop

	The catalog for the shop follows this logic:
		{'item name' : [quantity avaliable, item price]}
'''
class Shop:

	def __init__(self, name, catalog):
		self.name = name
		self.catalog = catalog

	def __str__(self):
		return f'Shop: {self.name} \n catalog: {self.catalog}'

	# returns the catalog of the shop
	def get_catalog(self):
		return self.catalog

	# returns the name of the shop
	def get_shop_name(self):
		return self.name

	# Returns the price of the given item.
	def get_item_price(self, item_name):
		try:
			return f'Price of item: {item_name}: ${self.catalog[item_name][1]}'
		except:
			print('Item does not exist.')

	''' 
	basic implementation of buying items, just looks at whether the item to be bought exist or not.
	If the item is found, reduce the avaliable amount and return the updated catalog.
	'''
	def buy_item(self, item_name):
		try:
			if self.catalog[item_name][0] > 0:
				self.catalog[item_name][0] = self.catalog[item_name][0] - 1
				return self.catalog
			else:
				print(f'Item {item_name} is currently unavaliable.')
				return self.catalog
		except:
			print('Invalid entry')


shop = Shop('ice cream wonderland', {'dull sword' : [2, 10], 'broken shield' : [1, 10], 'cap' : [2, 10]})
print(shop.get_item_price('dull sword'))



