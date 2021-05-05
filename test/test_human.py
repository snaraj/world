'''
	Test Suite for test all components of 'Human'.
'''
from unittest.mock import patch

from humans.human import Human

class TestHumanCreation:
	
	# @patch allows to test abstract classes without overriding abstract methods.
	@patch("test_human.Human.__abstractmethods__", set())
	def test_human_has_default_inventory(self):
		test_human = Human()
		for k,v in test_human.inventory.items():
			assert(v == None)