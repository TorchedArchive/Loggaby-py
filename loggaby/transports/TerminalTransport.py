from .Transport import Transport

class TerminalTransport(Transport):
	def __init__(self, color=True):
		Transport.__init__(self, color=color)

	def transmit(self, *args, **kwargs):
		print(*args, **kwargs)