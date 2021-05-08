import uuid

from humans.human import Human

class Town:
	#towns should have shops as well.
	roles_directory = {
		'base' : []
	}
	
	def __init__(self, 
		name='Unknown', 
		population=0):

		self.name = name
		self.population = population
		self.town_identifier = uuid.uuid4().int


	def __repr__(self):
		return 'Town(%r, %r, %r, %r)' % (self.name, self.population, self.roles_directory, self.town_identifier)
	
	def __str__(self):
		return 'Welcome to {self.name}'
	
	# adds a role to roles directory as long as it is a string.
	def create_role(self, role_name: str):
		assert isinstance(role_name, str), 'Invalid Role.'
		self.roles_directory[role_name] =  ''

	# adds a Human to the role.
	def add_to_role(self, Human, *args):
		for arg in args: 
			if arg in self.roles_directory:
				self.roles_directory[str(arg)] = Human
			else:
				return 'Unable to add {Human.get_human_name} to role {arg}'