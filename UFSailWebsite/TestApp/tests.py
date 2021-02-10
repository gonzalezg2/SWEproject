from django.test import TestCase

# inherits from Django TestCase class
class ExampleTestCase(TestCase):
	# overriden method, performs any preliminary work before running test cases
	def setUp(self): 
		pass

	def testCase1(self):
		pass

	def testCase2(self):
		pass