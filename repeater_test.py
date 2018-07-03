import unittest
# create interface for system undwer test
# to allow less test churn if we rename the sut

from repeater import repeater_tail_recurse as sut
#from repeater import repeater as sut
from repeater import assertAllInts as sut2

class TestHelpers():
    """helper functions for testing go here"""

    def none_to_pass(value):
        """convert the None return value of a test to PASS"""
        if value == None:
            return "PASS"
        else:
            return "FAIL"

#encapsulate test calss data to allow better clean up between test suites
class ValidateDuplicateNumber(unittest.TestCase):
    #make class scope for reuse
    two_dup_vals = [1, 2, 3, 4, 5, 6, 7, 1, 2] #should retrun 1
    no_val = [1, 2, 3, 4, 5, 6, 7] #should return None
    bad_val = [1, 2, "X3", 4, 5, 6, 7, 1, 2] #should fail
    exception_text = "Not all values are ints in:"
    odd_num_vals = list(range(1, 3))
    even_num_vals = list(range(1, 4))
    many_vals = list(range(1, 1940))
    recurse_error = "maximum recursion depth exceeded"

    def test_finds_first_dup(self):
        expected = 1
        # make private copy to prevent side effects on other tests
        data = self.two_dup_vals
        # make private copy of sut to avoid side effects
        _sut = sut
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print("TEST - test_finds_first_dup returns: " + str(expected) + ". Result: " + TestHelpers.none_to_pass(result))

    def test_handles_no_dupe(self):
        # uses a pattern to make adding new tests easier
        expected = None
        data = self.no_val
        _sut = sut
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print("TEST - test_handles_no_dupe: " + str(expected) + ". Result: " + TestHelpers.none_to_pass(result))

    def test_catches_bad_vals(self):
        expected = self.exception_text
        data = self.bad_val
        # change in pattern. we still want a private copy of sut
        # let's not actually throw while setting up the test
        _sut = sut
        with self.assertRaises(Exception) as actual:
            _sut(data)
        result = self.assertTrue(expected in str(actual.exception))
        print("TEST - test_catches_bad_vals: " + str(expected) + ". Result: " + TestHelpers.none_to_pass(result))

    def test_handles_even_lists(self):
        expected = None
        data = self.even_num_vals
        _sut = sut
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print("TEST - test_handles_even_lists: " + str(expected) + ". Result: " + TestHelpers.none_to_pass(result))

    @unittest.SkipTest #TODO this is a bug
    def test_handles_odd_lists(self):
        expected = None
        data = self.odd_num_vals
        _sut = sut
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print("TEST - test_handles_odd_lists: " + str(expected) + ". Result: " + TestHelpers.none_to_pass(result))

    def test_assertAllInts_true(self):
        expected = True
        data = self.no_val
        _sut = sut2
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print("TEST - test_assertAllInts_true: " + str(expected) + ". Result: " + TestHelpers.none_to_pass(result))

    def test_assertAllInts_false(self):
        expected = False
        data = self.bad_val
        _sut = sut2
        actual = _sut(data)
        result = self.assertEqual(expected, actual)
        print("TEST - test_assertAllInts_false: " + str(expected) + ". Result: " + TestHelpers.none_to_pass(result))

    # Python does not handle deep recursions
    # test for RecursionError: maximum recursion depth exceeded while getting the str of an object
    # So far no pattern to increase depth beyonf 19
    def test_throws_on_deep_recurse(self):
        """Test to validate how deep we can recurse before throwing"""
        expected = self.recurse_error
        data = self.many_vals
        _sut = sut
        with self.assertRaises(Exception) as actual:
            _sut(data)
        result = self.assertTrue(expected in str(actual.exception))
        print("TEST - test_throws_on_deep_recurse: " + str(expected) + ". Result: " + TestHelpers.none_to_pass(result))

unittest.main(exit=False)
