import random
from noose import Noose

def build_word_list(filename):
    """Returns a list of words from the given file
    
    Each word in the file should stored on a separate line. The lines are trimmed 
    to remove trailing spaces and line returns. 
    
    Example: build_word_list('short.txt') returns the 10 element list of words
    ['the','be','to','of','and','a','in','that','have','it'].
    
    Precondition: filename is the name of a text file storing a list of words.
    
    Enforced Precondition: filename is a string"""
    assert type(filename) == str, 'filename is not a string'

    accumulator = []
    with open(filename) as words:
	    for line in words: accumulator.append(line.strip().lower())
	    # Using strip here as defined by textbook (pg 98)
    return accumulator

word_list = build_word_list('words.txt')


def word_list_by_size(words, size):
    """Returns the elements of words that have length size
    
    The words in the resulting list should be in the same order as the original list.
    
    Example: word_list_by_size(['a', 'at', 'axe', 'by'], 2) returns ['at','by']
    
    Precondition: words is a list of strings. size is a positive int.
    
    Enforced Precondition: words a list. size is a positive int."""
    assert type(words) == list, 'words is not a list'
    assert type(size) == int, 'size is not an int'
    assert size > 0, 'size is not positive'

    return filter(lambda x: len(x)==size, words)

class Game:
	def __init__(self, lives=6):
		self.guesses_remain = lives
		self.won     = False
		self.lost    = False
		self.word    = random.choice(word_list)
		self.guesses = []
		self.noose  = Noose()

	def __str__(self):
		status = str(self.noose)+2*'\n'
		for char in self.word:
			if char in self.guesses: status += char + " "
			else: status += "_" + " " 

		letters = ""
		for char in self.wrong_guesses(): letters += char
		return status + "\n" + letters + "\nGuesses left: " + str(self.guesses_remain)

	def wrong_guesses(self):
		wrong = []
		for char in self.guesses:
			if char not in self.word: wrong.append(char)
		return wrong

	def guess(self, char):
		assert type(char) == str
		assert len(char) == 1
		assert char.isalpha()
		char = char.lower()
		assert char not in self.guesses

		self.guesses.append(char)
		if char not in self.word: self.guesses_remain -= 1

		self.noose.set_state( 6 - self.guesses_remain )

	def game_over(self):
		if self.guesses_remain <= 0:
			self.lost = True
			return True

		for char in self.word:
			if char not in self.guesses: return False

		self.won = True

		return True

def clear_screen(lines=5):
	print lines*"\n"

def play():
	game = Game()

	clear_screen()
	print game

	while not game.game_over():
		guess = raw_input('Please enter a guess: ')
		try:
			clear_screen()
			game.guess(guess)
		except AssertionError:
			print "Please enter valid input."
		print game

	if game.lost: print "The word was "+game.word+"\nBetter luck next time!"
	if game.won: print "Congratulations!"


play()

















