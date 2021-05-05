from humans.roles.warrior.warrior import Warrior
from tribe.tribe import Tribe

class TestWarriorCreation():
	# Testing the __init__ for creating a default warrior with default name and age.
	def test_default_warrior_creation(self):
		warrior = Warrior()
		assert 'unknown warrior', warrior.name
		assert 'unknown age', warrior.age

	# Testing __init__ with custom params, no default
	def test_custom_warrior_creation(self):
		warrior = Warrior('Warrior #1', 25)
		assert 'Warrior #1', warrior.name
		assert 25, warrior.age

	''' 
	A new warrior should have base stats of combat abilities : 5, and inherit the rest from
	the base human class. In this case, the default base stats for a human are intelligence : 0
	and strength : 0.
	'''
	def test_default_warrior_attribute_tree(self):
		warrior = Warrior()
		assert warrior.warrior_attribute_tree['combat abilities'] == 5
		assert warrior.warrior_attribute_tree['intelligence'] == 0
		assert warrior.warrior_attribute_tree['strength'] == 0

class TestWarriorInventory():
	'''
	Warrior should have the same default inventory as human, 4 slots and all empty.
	'''
	def test_default_warrior_inventory(self):
		warrior = Warrior()
		assert warrior.inventory == {0: None, 1 : None, 2: None, 3: None}

	'''
	warrior.add_to_inventory() takes in an item (string) and the amount. it then replaces an empty
	entry with that new item as long as there are empty entries, otherwise it doesn't allow the new
	item to be added.

	Empty entries are those that have None as a value.
	'''

	# Adding a single item to a default inventory
	def test_warrior_add_to_empty_inventory(self):
		warrior = Warrior()
		warrior.add_to_inventory('dagger', 1)
		assert warrior.inventory == {1:None, 2:None, 3:None, 'dagger':1}

	# Adding a single item to a non empty inventory
	def test_warrior_add_to_non_empty_inventory(self):
		warrior = Warrior()
		warrior.add_to_inventory('dagger', 1)
		warrior.add_to_inventory('sword', 2)
		assert warrior.inventory == {2:None, 3:None, 'dagger':1, 'sword':2}

	# Adding a single item to a full inventory should simply return 'Inventory is full.'
	def test_warrior_add_to_full_inventory(self):
		warrior = Warrior()
		
		warrior.add_to_inventory('dagger', 2)
		warrior.add_to_inventory('sword', 1)
		warrior.add_to_inventory('cape', 1)
		warrior.add_to_inventory('shield', 1)

		result = warrior.add_to_inventory('lance', 1)
		assert result == 'Inventory is Full.'













