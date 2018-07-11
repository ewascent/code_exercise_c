def none_to_pass(value):
    """Takes the value None and returns value of a test to PASS"""
    if value is None:
        return "PASS"
    return "FAIL"

def print_result(test_name, expected, result):
    """Helper function to print test results, maybe I should learn to use unittest better"""
    print("TEST - " + test_name + ": " + str(expected) + ". Result: " + none_to_pass(result))
