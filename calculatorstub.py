
import unittest
from calculator import String_Calculator


class TestAddStringNumbers(unittest.TestCase):
    """Tests for `_string_calculator` function."""

    def test_incorrect_input_types(self) -> None:
        """Test that non-string inputs fail"""
        testJob = String_Calculator()
        incorrect_inputs = [
            None,
            42,
            3.1415,
            [],
            {}
        ]
        for input_ in incorrect_inputs:
            self.assertRaises(TypeError, testJob.string_calculator, input_)

    def test_empty_string(self) -> None:
        """Test empty string as input"""
        testJob = String_Calculator()
        input_ = ""
        expected = 0
        actual = testJob.string_calculator(input_)
        self.assertEqual(expected, actual)

    def test_1_number(self) -> None:
        """Test a single number as input"""
        testJob = String_Calculator()
        input_ = "42"
        expected = 42
        actual = testJob.string_calculator(input_)
        self.assertEqual(expected, actual)

    def test_2_numbers(self) -> None:
        """Test 2 numbers as input"""
        testJob = String_Calculator()
        input_ = "42,99"
        expected = 141
        actual = testJob.string_calculator(input_)
        self.assertEqual(expected, actual)

    def test_many_numbers(self) -> None:
        """Test many numbers as input"""
        testJob = String_Calculator()
        input_ = "1,2,3,4,5,6,7,8,9,10"
        expected = 55
        actual = testJob.string_calculator(input_)
        self.assertEqual(expected, actual)

    def test_negative_numbers(self) -> None:
        """Test that input with negative numbers fails"""
        testJob = String_Calculator()
        input_ = "-1"
        self.assertRaises(ValueError, testJob.string_calculator, input_)
        input_ = "-1,2,-3"
        self.assertRaises(ValueError, testJob.string_calculator, input_)

    def test_numbers_greater_than_1000(self) -> None:
        """Test that numbers greater than 1000 are ignored"""
        testJob = String_Calculator()
        input_ = "1,1001,2"
        expected = 3
        actual = testJob.string_calculator(input_)
        self.assertEqual(expected, actual)
        input_ = "1001,2001,3001"
        expected = 0
        actual = testJob.string_calculator(input_)
        self.assertEqual(expected, actual)

    def test_newline_in_delimiters(self) -> None:
        """Test that input with newline in delimiter placement pass"""
        testJob = String_Calculator()
        input_ = "1\n,2\n,3"
        expected = 6
        actual = testJob.string_calculator(input_)
        self.assertEqual(expected, actual)


    def test_custom_delimiters(self) -> None:
        """Test that custom delimiters can be used with `//delim1,delim2\n` syntax"""
        testJob = String_Calculator()
        input_ = "//***,@\n1***2@3"
        expected = 6
        actual = testJob.string_calculator(input_)
        self.assertEqual(expected, actual)
        input_ = "//***,&&\n1***2&&3"
        expected = 6
        actual = testJob.string_calculator(input_)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()