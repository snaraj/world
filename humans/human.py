'''
Defines the blueprint for a human.
'''
from abc import ABC, abstractmethod

import uuid

from .inventory.inventory import Inventory

class Human(ABC):

	def __init__(self):
		self.human_identifier = str(uuid.uuid4().int)
		self.human_attribute_tree = self.HumanAttributeTree().human_attribute_tree_dictionary
		self.inventory = Inventory().content

	# Abstract getters common across all humans
	@abstractmethod
	def get_name(self):
		pass

	@abstractmethod
	def get_age(self):
		pass

	@abstractmethod
	def add_to_inventory(self):
		pass

	def get_human_identifier(self):
		return self.human_identifier

	class HumanAttributeTree():

		human_attribute_tree_dictionary = {
			'intelligence' : 0,
			'strength': 0
		}

		def __init__(self, 
					intelligence = human_attribute_tree_dictionary['intelligence'], 
					strength = human_attribute_tree_dictionary['strength']):

			self.intelligence = intelligence
			self.strength = strength

		def __str__(self):
			return 'Displaying human attribute tree: \n intelligence: {intelligence} - strength: {strength}'.format(**self._human_attribute_tree_dictionary)

		def __getitem__(self, attribute):
			try: 
				return self.human_attribute_tree_dictionary[attribute]
			except:
				return 'Attribute does not exist.'
