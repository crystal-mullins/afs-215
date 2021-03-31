import fizzbuzzkata
import unittest
class TestFizzBuzz(unittest.TestCase):

    def test_multiple_of_three(self):
       self.assertEqual(fizzbuzzkata.process(6), 'Fizz')

    def test_multiple_of_five(self):
        self.assertEqual(fizzbuzzkata.process(20), 'Buzz')

    def test_multiple_of_six(self):
        self.assertEqual(fizzbuzzkata.process(30), 'Fizz')

    def test_multiple_of_ten(self):
        self.assertEqual(fizzbuzzkata.process(100), 'Buzz')

    # def test_fizzbuzz(self):
    #     self.assertEqual(fizzbuzzkata.process(15), 'FizzBuzz')

    def test_regular_numbers(self):
        self.assertEqual(fizzbuzzkata.process(2), 2)
        self.assertEqual(fizzbuzzkata.process(98), 98)
        

if __name__ == '__main__':
    unittest.main()

#     import fizzbuzz
# import unittest
# class TestFizzBuzz(unittest.TestCase):

#     def test_multiple_of_three(self):
#        self.assertEqual(fizzbuzz.process(6), 'Fizz')

#     def test_multiple_of_five(self):
#         self.assertEqual(fizzbuzz.process(20), 'Buzz')

#     def test_fizzbuzz(self):
#         self.assertEqual(fizzbuzz.process(15), 'FizzBuzz')

#     def test_regular_numbers(self):
#         self.assertEqual(fizzbuzz.process(2), 2)
#         self.assertEqual(fizzbuzz.process(98), 98)
        

# if __name__ == '__main__':
#     unittest.main()
