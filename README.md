# code_exercise_c
Updated code exercise. Find the first duplicate number.

## TODO
Fix the tail recursion if possible.
http://code.activestate.com/recipes/474088-tail-call-optimization-decorator/

One test is failing. Need to fix that issue in the code

## Usage
Added a few updates to capture some ideas from our session. To see the code in action run the tests

> python .\repeater_test.py

>> TEST - test_assert_all_ints_false: False. Result: PASS

>> TEST - test_assert_all_ints_true: True. Result: PASS

>> TEST - test_catches_bad_vals: Not all values are ints in:. Result: PASS

>> TEST - test_finds_first_dup returns: 1. Result: PASS

>> TEST - test_handles_no_dupe: None. Result: PASS

>> ----------------------------------------------------------------------

>> Ran 5 tests in 0.021s

To use this to run the code directly

> python __main__.py

If you want to compare the original function (repeater) to the new function (repeater_tail_recurse), swap the comment on lines 6 and 7 in repeater_test.py. That swaps the system under test. Also shows why I alias the function names to allow the test code to have less dependancy on the functional code.
