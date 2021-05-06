'''
	Defines the blueprint for a human.
'''
from abc import ABC, abstractmethod

import uuid

from .inventory.inventory import Inventory

class Human(ABC):

	def __init__(self):
		# Unique identifier generated per human, in place to avoid name confusions.
		self.human_identifier = str(uuid.uuid4().int)
		# Initialize a base attribute tree, which is inherited by Human subclasses.
		self.human_attribute_tree = self.HumanAttributeTree().human_attribute_tree_dictionary
		# Initialize a base Inventory which holds 4 spaces and its empty.
		self.inventory = Inventory().content
		# Human starts off with $0.
		self.coins = 0

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
			'strength': 0,
			'health': 100
		}

		def __init__(self, 
					intelligence = human_attribute_tree_dictionary['intelligence'], 
					strength = human_attribute_tree_dictionary['strength'],
					health = human_attribute_tree_dictionary['health']):

			self.intelligence = intelligence
			self.strength = strength
			self.health = health

		def __str__(self):
			return f'Displaying human attribute tree: intelligence: {self.intelligence} strength: {self.strength} health: {self.health}'

		def __getitem__(self, attribute):
			try: 
				return self.human_attribute_tree_dictionary[attribute]
			except:
				return 'Attribute does not exist.'
