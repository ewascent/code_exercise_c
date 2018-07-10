"""original module for finding the first matching number"""
def assert_all_ints(nums):
    """Data validation routine to ensure we are parsing an array of ints
    USAGE: if catch_nonint([1,2,3,"x", 5]: raise TypeError("Not all values are ints") )"""

    for num in nums:
        _num = str(num).lstrip().rstrip()
        is_good = None
        if isinstance(num, int) and is_good != False:
            is_good = True
        else:
            is_good = False
            return is_good
    return is_good

def repeater(nums):
    """USAGE x = repeater([1,2,3]; print(str(x) + " is the first repeated int"))"""
    val = None

    if not assert_all_ints(nums):
        raise TypeError("Not all values are ints in:" + str(nums))

#TODO: consider using enumerate here
    for index in range(0, len(nums)):
        for new_index in range((index + 1), len(nums)):
            if nums[new_index] == nums[index]:
                val = nums[index]
                return val
    return None
