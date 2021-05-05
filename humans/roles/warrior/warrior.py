from humans.human import Human

class Warrior(Human):
	#inherits from human
	def __init__(self, name, age, weapon):
		super().__init__(name, age)
		self.weapon = weapon
	
	def __str__(self):
		return f'name: {self.name} age: {self.age} weapon: {self.weapon}'

warrior = Warrior('heath', 10, 'claws')
print(warrior.human_attribute_tree)
