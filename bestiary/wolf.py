class Wolf:
	
	loot_table = {
		'bones' : 1,
		'wolf tooth' : 5,
		'wolf fur': 1
	}

	def __init__(self, health):
		self.health = health

	def __str__(self):
		return f'Wolf has {self.health} health.'

wolf = Wolf(120)
print(wolf)