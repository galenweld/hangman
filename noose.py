import os

sketch_directory = 'hangmen_ascii'


class Noose(object):
	"""print nooses"""
	def __init__(self):
		self._state = 0
		self.load_ascii()


	def inc(self):
		''' increase the number of limbs '''
		assert self._state < 6, 'Hangman is already fully hung.'
		self._state += 1
		self.load_ascii()


	def set_state(self, state):
		''' set state to int 0<= state <=6 '''
		assert int(state) <= 6 and int(state) >=0, "Invalid state"
		self._state = int(state)
		self.load_ascii()


	def __str__(self):
		return self._ascii

	def __repr__(self):
		return "<Noose instance with state {}>".format(self._state)

	def load_ascii(self):
		''' load ascii from file and return a string '''
		filename = "{}.txt".format(self._state)
		filename = os.path.join(sketch_directory, filename)

		s = ""
		with open(filename) as f:
			for line in f:
				s += line
		self._ascii = s