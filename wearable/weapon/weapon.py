class Weapon:
	
	def __init__(self, name, durability, weapon_attribute_tree_dictionary):
		self.name = name
		self.durability = durability
		self.weapon_attribute_tree_dictionary = weapon_attribute_tree_dictionary

	def __repr__(self):
		return 'Weapon(%r, %r, %r)' % (self.name, self.durability, self.weapon_attribute_tree_dictionary)

	def __str__(self):
		return f'Weapon \n name: {self.name} durability: {self.durability} stats: {self.weapon_attribute_tree_dictionary}'	

	class WeaponAttributeTree:
		
		weapon_attribute_tree_dictionary = {
			'dmg' : 0,
			'speed' : 0,
			'_type' : 'Unknown',
		}
		
		def __init__(self, 
			dmg = weapon_attribute_tree_dictionary['dmg'], 
			speed = weapon_attribute_tree_dictionary['speed'],
			_type = weapon_attribute_tree_dictionary['_type'] 
		):

			self.dmg = dmg
			self.speed = speed
			self._type = _type