import unittest
import functions

class Lab3TestCases(unittest.TestCase):
    def test_double_one(self):
        result = functions.double(2)
        expected = 4
        self.assertEqual(expected, result)

    def test_double_two(self):
        result = functions.double(3)
        expected = 6
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
# If test_double_one had been the only testing function, the tests would have passed the first time.
# Would that have meant that the code was correct? While waiting to demonstrate completion of the lab, ponder how many tests one might need to sufficiently test this function.
#My Answer: The code would've been correct if it meant test_double_one was the only code. There would be only one test to sufficiently test this function.