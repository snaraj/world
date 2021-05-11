'''
Test Suite for testing all components of a 'town'.
'''
from town.town import Town
from humans.roles.warrior.warrior import Warrior

#Everything that has to do with the creation of a town
class TestTownCreation:
    # Checks the behavior of the default constructor.
    def test_default_town_creation(self):
        town = Town()
        assert('Unknown', 0) == (town.name, town.population)

    # Checks the behavior of the regular constructor.
    def test_normal_town_creation(self):
    	town = Town('town X', 10)
    	assert('town X', 10) == (town.name, town.population)

#Everything that has to do with the functionability of the town Class
class TestTownFunctions:
	
	# Checks the behavior of adding a warrior to an existing role in town.roles_directory
	def test_adding_to_role(self):
		test_warrior = Warrior()
		test_warrior_identifier = test_warrior.get_human_identifier()
		test_town = Town()
		test_town.add_to_role(test_warrior, 'base')
		assert test_warrior in test_town.roles_directory.values()