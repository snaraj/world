'''
Defines the blueprint for a human.
'''
from abc import ABC, abstractmethod
import uuid

class Human(ABC):

	def __init__(self):
		self.human_identifier = str(uuid.uuid4().int)
		self.human_attribute_tree = self.HumanAttributeTree()

	def __str__(self):
		format_dictionary = {'name' : self.name,
							'age': self.age,
							'human_identifier' : self.human_identifier}

		return 'Human: #{human_identifier} - Name: {name} - Age: {age}'.format(**format_dictionary)

	def get_human_name(self):
		return self.name

	def get_human_age(self):
		return self.age

	def get_human_identifier(self):
		return self.human_identifier

	def get_name_from_human_identifier(self, human_identifier):
		return 

	class HumanAttributeTree():

		_human_attribute_tree_dictionary = {
			'intelligence' : 0,
			'strength': 0
		}

		def __init__(self, 
					intelligence = _human_attribute_tree_dictionary['intelligence'], 
					strength = _human_attribute_tree_dictionary['strength']):

			self.intelligence = intelligence
			self.strength = strength

		def __str__(self):
			return 'Displaying known human attribute tree: \n intelligence: {intelligence} - strength: {strength}'.format(**self._human_attribute_tree_dictionary)

		def __getitem__(self, attribute):
			try: 
				return self._human_attribute_tree_dictionary[attribute]
			except:
				return 'Attribute does not exist.'

human = Human()
print(human.human_attribute_tree['intelligence'])