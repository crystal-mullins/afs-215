import unittest

class Test_TestStuff(unittest.TestCase):

    def test_add_two_numbers(self):
        self.assertEqual(4, 4)

    def test_add_two_numbers_no(self):
        self.assertNotEqual(4, 4)


    def test_add_two_numbers(first, second):
        return first + second


if __name__ == '__main__':
	unittest.main()

# import unittest
# from fizzbuzz import FizzBuzz

# class TestFizzBuzz(unittest.TestCase):

# 	def test_simple_should_return_the_number(self):
# 		self.assertEqual(FizzBuzz(1), 1)
# 		self.assertEqual(FizzBuzz(2), 2)
# 		self.assertEqual(FizzBuzz(4), 4)

# 	def test_multiple_3_should_return_fizz(self):
# 		self.assertEqual(FizzBuzz(3), "fizz")
# 		self.assertEqual(FizzBuzz(9), "fizz")

# 	def test_multiple_5_should_return_buzz(self):
# 		self.assertEqual(FizzBuzz(5), "buzz")
# 		self.assertEqual(FizzBuzz(10), "buzz")
	
# 	def test_multiple_3_and_5_should_return_fizzbuzz(self):
# 		self.assertEqual(FizzBuzz(15), "fizzbuzz")
# 		self.assertEqual(FizzBuzz(30), "fizzbuzz")
		

# if __name__ == '__main__':
# 	unittest.main()


     