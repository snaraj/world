from tribe import Tribe
from humans.human import Human

import string
import random

class Directory:
	def __init__(self, name='Unknown', content={}):
		self.name = name
		self.content = content

	def print_directory(self):
		for key, value in self.content.items():
			print(key, '::', value)

	#Could replace this with a .txt file that has a name pool, or pull from a name API
	def populate_directory(self):
		letters = string.ascii_letters
		for i in range(10):
			name = (''.join(random.choice(letters) for i in range(10)))
			human = Human(name)
			self.content[name] = human.human_identifier




dir = Directory()
dir.populate_directory()
print(dir.print_directory())