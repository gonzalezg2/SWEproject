from django.test import TestCase
from django.test import SimpleTestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from math import sqrt

# MAKE SURE TEST CASES START WITH 'test'!!!!!!!!

# Use this if you don't need the database (inherit from SimpleTestCase)
class ExampleTestCases(SimpleTestCase):
	# overriden method, performs any preliminary work before running test cases
	def setUp(self): 
		self.x = 1
		self.y = 2

	# shows how to use values from setUp
	def testCase1(self):
		self.assertEquals(self.x, self.y - 1)

	# basic math test
	def testCase2(self):
		a = 1
		b = -3
		c = 2
		root1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
		root2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
		self.assertEquals(0, a*root1**2 + b*root1 + c)


# Use this if you need the database (makes a mock database and inherits from TestCase)
class ExampleTestCasesWithDatabase(TestCase):
	
	def setUp(self):
		self.adminUser = User.objects.create_user(username="joe")

	def testDatabase(self):
		if User.objects.filter(username="joe").exists():
			print("User joe created successfully")
		else:
			raise Exception("User not created")