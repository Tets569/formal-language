from itertools import product
# from functools import reduce


class Symbol:
	'''uses "." to denote end of letter for reading complicated words'''
	def __init__(self, name, symbol=None):
		if symbol is None:
			symbol = name

		self.name = str(name) 
		self.symbol = str(symbol)

	def __str__(self):
		return str(self.symbol)

	def __repr__(self):
		return '.' + str(self.symbol) + '.'

	def __len__(self):
		return len(self.symbol) # - 1 for the '.' at the end

	def __add__(self, other):
		name = str(self.name) + str(other.name)
		symbol = str(self.symbol) + str(other.symbol)
		return Symbol(name, symbol)

	def __eq__(self, other):
		return self.symbol == other.symbol

	@staticmethod
	def spaceSymbol():
		return Symbol('_', ' ')
# class Spacename(name):
# 	def __init__(self):
# 		super(self.__class__, self).__init__('_', ' ')

	@staticmethod
	def emptySymbol():
		return Symbol('', '')
# class Empty(name):
# 	def __init__(self):
# 		super(self.__class__, self).__init__(name='', symbol='')



class Alphabet:
	'''
		(Note: EmptyStr is NOT in Alphabet.  It is a word.)
		TODO: Distinguish Words from Symbols???
		self.letters -> {Symbol(), Symbol(), ...}
	'''
	def __init__(self, alphabet):
		letters = []

		for alpha in alphabet:
			if not isinstance(alpha, Symbol):
				alpha = Symbol(alpha)
			letters.append(alpha)

		self.letters = letters

	def has_word(self, letters):
		for letter in letters:
			if not isinstance(letter, Symbol):
				letter = Symbol(letter)
			if letter not in self.letters:  # and letter != Symbol.emptySymbol():
				return False
		return True
	
	def words_of_len_n(self, n):  
		''' 
			__product(*args, repeat=1)__
		'''
		if n < 0:
			raise ValueError('')

		words = []
		letters = map(lambda x: x.symbol, self.letters)  # vs generator?

		if n == 1:
			words = [letter for letter in letters]

		elif n > 1:
			prods = product(letters, repeat=n)

			for word in prods:
				words.append(reduce(lambda x,y: x + y, word))
		
		return words

	def __eq__(self, other):
		'''
			Should be defined in a way s.t.:
				Sigma^0 == set(EmptyString)
				Sigma^1 != Sigma due to typing
				Sigma^* == set(Sigma^0 U Sigma^1 U ...)
		'''
		# if not isinstance(other, Alphabet):
		# 	raise ValueError('')
		return self.letters == other.letters


class Language:
	'''
		1) Set of words from Sigma ^ *
		2) Subset of Sigma ^ * 
		3) Language "over" Sigma
		4) L is Language over E2 for each E2 superset(E) (Because still a subset of all supersets)
	'''


class DFA:
	'''
		Q - Set of states, finite
		E - Set of input symbols, finite
		d - transition function
		q0 - Initial state
		F - Accepted final states
	'''