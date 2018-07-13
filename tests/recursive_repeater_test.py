"""Unit tests"""
import unittest2 as unittest
from src.recursive_repeater import repeater_recurse as sut
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

    def test_recurse_repeater_finds_first_dup(self):
        """Find the first dupe in the list with several dupes - recurse"""
        expected = self.two_dup_vals[0]
        data = self.two_dup_vals
        _sut = sut
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print_result("test_finds_first_dup returns", expected, result)

    def test_recurse_repeater_handles_no_dupe(self):
        """ensure we can handle arrays with no dupes"""
        expected = None
        data = self.no_val
        _sut = sut
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print_result("test_handles_no_dupe", expected, result)

    def test_recurse_repeater_catches_bad_vals(self):
        """test we are handling bad value checking correctly.
        Since this tests exceptions we wrap it in wiht"""
        expected = self.exception_text
        data = self.bad_val
        _sut = sut
        with self.assertRaises(Exception) as actual:
            _sut(data)
        result = self.assertTrue(expected in str(actual.exception))
        print_result("test_catches_bad_vals", expected, result)

    def test_recurse_repeater_handles_even_lists(self):
        """Code handles iteration over even numbers of items in list"""
        expected = None
        data = self.even_num_vals
        _sut = sut
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print_result("test_handles_even_lists", expected, result)

    def test_recurse_repeater_handles_odd_lists(self):
        """Code handles iteration over odd numbers of items in list"""
        expected = None
        data = self.odd_num_vals
        _sut = sut
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print_result("test_handles_odd_lists", expected, result)

unittest.main(exit=False)
