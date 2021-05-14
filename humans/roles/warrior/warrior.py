from humans.human import Human

class Warrior(Human):

	'''
	every warrior should have:
		Unique id inherited from Human
		a name
		age
		base_dmg (basically dps)
	'''
	def __init__(self, name='Unknown', age=0, base_dmg=0):
		# Inherits human attributes as well as the human_attribute_tree.
		super().__init__()
		# Adding the attribute value 'combat abilities' to the human_attribute_tree.
		self.warrior_attribute_tree = self.human_attribute_tree | {'combat abilities' : 5}
		# Normal warrior/human atttributes, maybe put this in Human?
		self.name = name
		self.age = age
		self.base_dmg = base_dmg

	# Unambiguous Warrior Object representation.
	def __repr__(self):
		return 'Warrior({%r}, {%r}, {%r}, {%r}' % (self.name, self.age, self.warrior_attribute_tree, self.coins)
	
	# Readable Warrior Object representation.	
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

	# ALL warriors should be able to peform a set of commands.
	class Behavior:

		def attack(self, target):
			target.health = target.health - self.base_dmg




















