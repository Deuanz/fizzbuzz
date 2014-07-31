import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_number_is_divisible_by_3_should_return_fizz(self):
        fizzbuzz = FizzBuzz()
        result = fizzbuzz.take(3)
        self.assertEqual(result, 'Fizz')


class FizzBuzz:
    def take(self, number):
        return 'Fizz'


if __name__ == '__main__':
    unittest.main()
