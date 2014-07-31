import unittest
import xmlrunner


class FizzBuzzTest(unittest.TestCase):
    def test_number_is_divisible_by_3_should_return_fizz(self):
        fizzbuzz = FizzBuzz()
        result = fizzbuzz.take(3)
        self.assertEqual(result, 'Fizz')

    def test_number_is_divisible_by_5_should_return_fizz(self):
        fizzbuzz = FizzBuzz()
        result = fizzbuzz.take(5)
        self.assertEqual(result, 'Buzz')


class FizzBuzz:
    def take(self, number):
        return 'Fizz'


if __name__ == '__main__':
    #unittest.main()
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
