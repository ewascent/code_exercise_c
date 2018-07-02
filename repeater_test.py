import unittest
# create interface for system undwer test
# to allow less test churn if we rename the sut
from repeater import repeater as sut
from repeater import assertAllInts as sut2

class TestHelpers():
    def none_to_pass(value):
        if value == None:
            return "PASS"
        else:
            return "FAIL"

#encapsulate test calss data to allow better clean up between test suites
class ValidateDuplicateNumber(unittest.TestCase):
    #make class scope fpor reuse
    two_dup_vals = [1,2,3,4,5,6,7,1,2] #should retrun 1
    no_val = [1,2,3,4,5,6,7] #should return None
    bad_val = [1,2,"X3",4,5,6,7,1,2] #should fail
    exception_text = "Not all values are ints in:"

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

unittest.main(exit=False)
