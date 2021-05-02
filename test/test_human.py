'''
	Test Suite for test all components of 'Human'.
'''

from humans.human import Human

class TestHumanCreation:
	# Check the behavior of the default Human constructor
	def test_default_human_creation(self):
		test_human = Human()
		assert('Unknown', None) == (test_human.name, test_human.age)