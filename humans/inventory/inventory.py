class Inventory:
	def __init__(self, content={}, size=4):
		keys = [x for x in range(size)]
		self.content = dict.fromkeys(keys, None)

	def display_inventory(self):
		for key, value in self.content.items():
			print(key, '::', value)
