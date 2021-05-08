'''
Test Suite for testing all components of a 'town'.
'''
from unittest.mock import patch

from town.town import town
from humans.human import Human

#Everything that has to do with the creation of a town
class TestTownCreation:
    # Checks the behavior of the default constructor.
    def test_default_town_creation(self):
        town = Town()
        assert('Unknown', 0, 'Unknown') == (town.name, town.population, town.name_of_founder)

    # Checks the behavior of the regular constructor.
    def test_normal_town_creation(self):
    	town = Town('town X', 10)
    	assert('town X', 10) == (town.name, town.population)

#Everything that has to do with the functionability of the town Class
class TestTownFunctions:
	
	# Checks the behavior of adding a Human to an existing role in town.roles_directory
	@patch("test_human.Human.__abstractmethods__", set())
	def test_adding_to_role(self):
		test_human = Human()
		test_human_identifier = test_human.get_human_identifier()
		test_town = Town()
		test_town.add_to_role(test_human, 'base')
		assert test_human.human_identifier in test_town.roles_directory.values()







