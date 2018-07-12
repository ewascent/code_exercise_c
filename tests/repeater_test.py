"""Unit tests"""
import unittest2 as unittest
from src.recursive_repeater import repeater_recurse as sut
from src.repeater import assert_all_ints as sut2
from src.repeater import repeater as sut3
from test_helpers import print_result

#encapsulate test calss data to allow better clean up between test suites
class ValidateDuplicateNumber(unittest.TestCase):
    """validate functional aspects of each unit"""
    two_dup_vals = [1, 2, 3, 1, 2, 3] #should return 1
    no_val = list(range(11, 17)) #should return None
    bad_val = [1, 2, "X3", 4, 5, 6, 7, 1, 2] #should fail
    exception_text = "Not all values are ints in:"
    odd_num_vals = list(range(11, 13))
    even_num_vals = list(range(11, 14))
    many_vals = list(range(1, 1940))
    recurse_error = "maximum recursion depth exceeded"

    def test_recurse_repeater_finds_first_dup(self):
        """Find the first dupe in the list with several dupes - recurse"""
        expected = self.two_dup_vals[0]
        data = self.two_dup_vals
        _sut = sut
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print_result("test_finds_first_dup returns", expected, result)

    def test_repeater_finds_first_dup(self):
        """Find the first dupe in the list with several dupes - non-recurse"""
        expected = self.two_dup_vals[0]
        data = self.two_dup_vals
        _sut = sut3
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print_result("test_finds_first_dup returns", expected, result)

    def test_handles_no_dupe(self):
        """ensure we can handle arrays with no dupes"""
        expected = None
        data = self.no_val
        _sut = sut
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print_result("test_handles_no_dupe", expected, result)

    def test_catches_bad_vals(self):
        """test we are handling bad value checking correctly.
        Since this tests exceptions we wrap it in wiht"""
        expected = self.exception_text
        data = self.bad_val
        _sut = sut
        with self.assertRaises(Exception) as actual:
            _sut(data)
        result = self.assertTrue(expected in str(actual.exception))
        print_result("test_catches_bad_vals", expected, result)

    def test_handles_even_lists(self):
        """Code handles iteration over even numbers of items in list"""
        expected = None
        data = self.even_num_vals
        _sut = sut
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print_result("test_handles_even_lists", expected, result)

    def test_handles_odd_lists(self):
        """Code handles iteration over odd numbers of items in list"""
        expected = None
        data = self.odd_num_vals
        _sut = sut
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print_result("test_handles_odd_lists", expected, result)

    def test_assert_all_ints_true(self):
        """Test that the data cleansing routine approves all ints"""
        expected = True
        data = self.no_val
        _sut = sut2
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print_result("test_assert_all_ints_true", expected, result)

    def test_assert_all_ints_false(self):
        """Test that the data cleansing routine detects errors"""
        expected = False
        data = self.bad_val
        _sut = sut2
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print_result("test_assert_all_ints_false", expected, result)

unittest.main(exit=False)
