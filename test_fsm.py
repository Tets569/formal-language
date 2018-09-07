import unittest
from FSM import Symbol, Alphabet

class Test_FSM(unittest.TestCase):
	def test_something(self):
		pass


### ------TEST-SUITE: SYMBOL
class Test_Symbol(unittest.TestCase):
	''''''
	@classmethod
	def setUpClass(cls):
		cls.a = Symbol('a')
		cls.b = Symbol('b')
		cls.abCaps = Symbol('AB')

		cls.abPlus = cls.a + cls.b
		# cls.abMinus = cls.a - cls.b !ERROR

	def test_init(self):
		self.assertEqual(self.a.name, 'a')
		self.assertEqual(self.a.symbol, 'a')

		self.assertEqual(self.b.name, 'b')
		self.assertEqual(self.b.symbol, 'b')

		self.assertEqual(self.abCaps.name, 'AB')
		self.assertEqual(self.abCaps.symbol, 'AB')

	def test_str(self):
		self.assertEqual(str(self.a), 'a')
		self.assertEqual(str(self.b), 'b')
		self.assertEqual(str(self.abCaps), 'AB')

	def test_repr(self):
		self.assertEqual(repr(self.a), '.a.')
		self.assertEqual(repr(self.b), '.b.')
		self.assertEqual(repr(self.abCaps), '.AB.')

	def test_add(self):
		self.assertEqual(self.abPlus.name, 'ab')
		self.assertEqual(self.abPlus.symbol, 'ab')
		self.assertEqual(str(self.abPlus), 'ab')
		self.assertEqual(repr(self.abPlus), '.ab.')

	def test_len(self):
		pass

	def test_eq(self):
		pass


class Test_SpaceSymbol(unittest.TestCase):
	''''''
	@classmethod
	def setUpClass(cls):
		cls.a = Symbol('a')
		cls.b = Symbol('b')
		cls.space = Symbol.spaceSymbol()
		cls.aSpace = cls.a + cls.space
		cls.spaceA = cls.space + cls.a

		cls.abSpace = cls.a + cls.space + cls.b

	def test_init(self):
		self.assertEqual(self.space.name, '_')
		self.assertEqual(self.space.symbol, ' ')

		self.assertEqual(self.aSpace.name, 'a_')
		self.assertEqual(self.aSpace.symbol, 'a ')

		self.assertEqual(self.spaceA.name, '_a')
		self.assertEqual(self.spaceA.symbol, ' a')


	def test_str(self):
		self.assertEqual(str(self.space), ' ')
		self.assertEqual(str(self.aSpace), 'a ')
		self.assertEqual(str(self.spaceA), ' a')


	def test_repr(self):
		self.assertEqual(repr(self.space), '. .')
		self.assertEqual(repr(self.aSpace), '.a .')
		self.assertEqual(repr(self.spaceA), '. a.')

	def test_add(self):
		self.assertEqual(self.abSpace.name, 'a_b')
		self.assertEqual(self.abSpace.symbol, 'a b')
		self.assertEqual(str(self.abSpace), 'a b')
		self.assertEqual(repr(self.abSpace), '.a b.')


class Test_EmptySymbol(unittest.TestCase):
	''''''
	@classmethod
	def setUpClass(cls):
		cls.a = Symbol('a')
		cls.b = Symbol('b')
		cls.empty = Symbol.emptySymbol()
		cls.aEmpty = cls.a + cls.empty
		cls.emptyA = cls.empty + cls.a

		cls.abEmpty = cls.a + cls.empty + cls.b

	def test_init(self):
		self.assertEqual(self.empty.name, '')
		self.assertEqual(self.empty.symbol, '')

		self.assertEqual(self.aEmpty.name, 'a')
		self.assertEqual(self.aEmpty.symbol, 'a')

		self.assertEqual(self.emptyA.name, 'a')
		self.assertEqual(self.emptyA.symbol, 'a')

	def test_str(self):
		self.assertEqual(str(self.empty), '')
		self.assertEqual(str(self.aEmpty), 'a')
		self.assertEqual(str(self.emptyA), 'a')

	def test_repr(self):
		self.assertEqual(repr(self.empty), '..')
		self.assertEqual(repr(self.aEmpty), '.a.')
		self.assertEqual(repr(self.emptyA), '.a.')

	def test_add(self):
		self.assertEqual(self.abEmpty.name, 'ab')
		self.assertEqual(self.abEmpty.symbol, 'ab')
		self.assertEqual(str(self.abEmpty), 'ab')
		self.assertEqual(repr(self.abEmpty), '.ab.')	
### ------TEST-SUITE: SYMBOL

### ------TEST-SUITE: ALPHABET
class Test_Alphabet(unittest.TestCase):
	''''''
	@classmethod
	def setUpClass(cls):
		cls.abcStr = Alphabet('abc')
		cls.abcLst = Alphabet(['a', 'b', 'c'])
		cls.abcSym = Alphabet([Symbol('a'), Symbol('b'), Symbol('c')])

	def test_init(self):
		letters = [Symbol('a'), Symbol('b'), Symbol('c')]
		# self.assertIn(Symbol('a'), self.abcStr.letters)
		self.assertEqual(letters, self.abcStr.letters)
		self.assertEqual(letters, self.abcLst.letters)
		self.assertEqual(letters, self.abcSym.letters)

	def test_has_word(self):
		self.assertTrue(self.abcStr.has_word('a'))
		self.assertTrue(self.abcStr.has_word('abc'))
		self.assertTrue(self.abcStr.has_word('aaccbb'))

	def test_words_of_len_n(self):
		symbols = [x.symbol for x in self.abcStr.letters]

		words = []
		self.assertEqual(words, self.abcStr.words_of_len_n(0))

		words = [x for x in symbols]
		self.assertEqual(words, self.abcStr.words_of_len_n(1))

		words = [x+y for x in symbols for y in symbols]
		self.assertEqual(words, self.abcStr.words_of_len_n(2))

		words = [x+y+z for x in symbols for y in symbols for z in symbols]
		self.assertEqual(words, self.abcStr.words_of_len_n(3))

	def test_eq(self):
		self.assertEqual(self.abcStr, self.abcLst)
		self.assertEqual(self.abcLst, self.abcSym)
		self.assertEqual(self.abcSym, self.abcStr)

		with self.assertRaises(AttributeError):
			bad = self.abcStr == self.abcStr.words_of_len_n(1)
### ------TEST-SUITE: ALPHABET


if __name__ == '__main__':
	unittest.main()

'''
	print(letter) --> uses __repr__
	print(letter,) --> uses __str__
'''