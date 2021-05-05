'''
Test Suite for testing all components of a 'tribe'.
'''
from unittest.mock import patch

from tribe.tribe import Tribe
from humans.human import Human

#Everything that has to do with the creation of a tribe
class TestTribeCreation:
    # Checks the behavior of the default constructor.
    def test_default_tribe_creation(self):
        tribe = Tribe()
        assert('Unknown', 0, 'Unknown') == (tribe.name, tribe.population, tribe.name_of_founder)

    # Checks the behavior of the regular constructor.
    def test_normal_tribe_creation(self):
    	tribe = Tribe('Tribe X', 10, 'Tribe X Captain')
    	assert('Tribe X', 10, 'Tribe X Captain') == (tribe.name, tribe.population, tribe.name_of_founder)

#Everything that has to do with the functionability of the Tribe Class
class TestTribeFunctions:
	
	# Checks the behavior of adding a Human to an existing role in tribe.roles_directory
	@patch("test_human.Human.__abstractmethods__", set())
	def test_adding_to_role(self):
		test_human = Human()
		test_human_identifier = test_human.get_human_identifier()
		test_tribe = Tribe()
		test_tribe.add_to_role(test_human, 'base')
		assert test_human.human_identifier in test_tribe.roles_directory.values()







