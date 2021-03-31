
# import unittest

# class Test_TestStuff(unittest.TestCase):

#     def test_add_two_numbers(self):
#         self.assertEqual(4, 4)

#     def test_add_two_numbers_no(self):
#         self.assertNotEqual(3, 4)


# def test_add_two_numbers(first, second):
#         return first + second


# if __name__ == '__main__':
# 	unittest.main()
import fizzbuzz
import unittest
class TestFizzBuzz(unittest.TestCase):

    def test_multiple_of_three(self):
       self.assertEqual(fizzbuzz.process(6), 'Fizz')

    def test_multiple_of_five(self):
        self.assertEqual(fizzbuzz.process(20), 'Buzz')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.process(15), 'FizzBuzz')

    def test_regular_numbers(self):
        self.assertEqual(fizzbuzz.process(2), 2)
        self.assertEqual(fizzbuzz.process(98), 98)
        

if __name__ == '__main__':
    unittest.main()
