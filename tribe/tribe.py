from collections import namedtuple
import uuid
from humans.human import Human

class Tribe:

	name = 'Unknown'
	name_of_founder = 'Unknown'
	tribe_description = 'Unknown'
	
	population = 0

	roles_directory = {
		'base' : []
	}
	
	def __init__(self, 
		name=name, 
		population=population, 
		name_of_founder=name_of_founder):

		self.name = name
		self.population = population
		self.name_of_founder = name_of_founder
		self.roles_directory['governing'] = self.name_of_founder
		self.tribe_identifier = uuid.uuid4().int

	# The following functions are used to display various details about the tribe.
	# __str__() prints general info about the tribe.
	def __str__(self):
		format_dictionary = {	'name' : self.name,
								'tribe_identifier': self.tribe_identifier, 
								'population' : self.population,
								'name_of_founder': self.name_of_founder}

		return 'Tribe name: {name} Unique Identifier: {tribe_identifier} ; founded by: {name_of_founder} ; with a population of: {population}'.format(**format_dictionary)
	
	def add_human_to_role(self, Human, *args):
		for arg in args: 
			if arg in self.roles_directory:
				self.roles_directory[str(arg)] = Human.human_identifier
			else:
				pass



ji_uxijui = Human("Samuel")
tribe = Tribe(population=1,name_of_founder=ji_uxijui.get_human_name())
tribe.add_human_to_role(ji_uxijui, 'lunch', 'warrior', 'merchant')

print(tribe)


