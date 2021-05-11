'''
 	Test suit for world/world.py 
'''
import unittest

from world import World
from town.town import Town
from humans.roles.warrior.warrior import Warrior
from industries.retail.shop import Shop
from bestiary.wolf import Wolf

# Test suit for the creation of world.
class TestWorldCreation:
	
	# Test that a world can be created from default params.
	def test_default_world_creation(self):
		test_world = World('world 1')
		assert repr(test_world) == '(World(\'world 1\'))'

#Test suit for adding elements to world.
class TestAddToWorld(unittest.TestCase):

	# Adding a new town to world.towns list.
	def test_add_town_to_world(self):
		test_world = World('world 1')
		test_town = Town()
		test_world.add_town(test_town)
		self.assertIn(test_town, test_world.towns)

	# Adding a new Shop to world.shops list.
	def test_add_shop_to_world(self):
		test_world = World('world 1')
		test_shop = Shop()
		test_world.add_shop(test_shop)
		self.assertIn(test_shop, test_world.shops)

	# Adding a new Warrior to world.humans dictionary.
	def test_add_warrior_to_world(self):
		test_world = World('world 1')
		test_warrior = Warrior()
		test_world.humans['warriors'] = test_warrior
		self.assertIn(test_warrior, test_world.humans.values())

	# Adding a new Wolf to world.bestiary dictionary.
	def test_add_wolf_to_world(self):
		test_world = World('world 1')
		test_wolf = Wolf()
		test_world.bestiary['wolfs'] = test_wolf
		self.assertIn(test_wolf, test_world.bestiary.values())











