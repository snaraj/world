class Wolf:
	
	def __init__(self, health=50, dmg=5):
		self.health = health
		self.dmg = dmg
		self.loot_table = {
			'bones' : 1,
			'wolf tooth' : 5,
			'wolf fur': 1
		}

	# Unambigous Wolf Object representation.
	def __repr__(self):
		return 'Wolf(%r, %r, %r)' % (self.health, self.dmg, self.loot_table)

	# Readable Wolf representation.
	def __str__(self):
		return 'It\'s a wolf!'