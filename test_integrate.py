# unit test case
import unittest

class animal:
	x = 'Lion'

class test:
	x = 'Lion'

class TestMethods(unittest.TestCase):
	# test function to test object equality of two valu
	def test_positive(self):
		firstValue = animal()
		secondValue = test()
		# error message in case if test case got failed
		message = "First value and second value are not evaluated to same object !"
		# assertIs() to check that if first & second evaluated to same object
		self.assertIs(firstValue, secondValue, message)

if __name__ == '__main__':
	unittest.main()
