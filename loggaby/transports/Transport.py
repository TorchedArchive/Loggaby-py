class Transport:
	def __init__(self, color=True):
		self.color = color

	def transmit(self):
		raise NotImplementedError