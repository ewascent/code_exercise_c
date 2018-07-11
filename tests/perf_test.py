import unittest
# create interface for system undwer test
# to allow less test churn if we rename the sut

from src.recursive_repeater import repeater_tail_recurse as sut
from src.repeater import repeater as sut2
from test_helpers import print_result

#encapsulate test calss data to allow better clean up between test suites
class PerfomranceTestsRepeater(unittest.TestCase):
    """Suite to ensure we are not hurting performance and can manage load/depth"""
    many_vals = list(range(1, 1940))
    recurse_error = "maximum recursion depth exceeded"

    def test_recursive_throws_on_deep_recurse(self):
        """Test to validate how deep we can recurse before throwing. Test for
        RecursionError: maximum recursion depth exceeded while getting the str of an object
        So far no pattern to increase depth beyond 19"""

        expected = self.recurse_error
        data = self.many_vals
        _sut = sut
        with self.assertRaises(Exception) as actual:
            _sut(data)
        result = self.assertTrue(expected in str(actual.exception))
        print_result("test_throws_on_deep_recurse", expected, result)

    def test_repeater_does_not_throw_on_long_list(self):
        """Test to show non-recursion exceeds list length of recursion"""

        expected = None
        data = self.many_vals
        _sut = sut2
        actual = _sut(data)
        result = self.assertTrue(expected == actual)
        print_result("test_throws_on_deep_recurse", expected, result)

unittest.main(exit=False)
