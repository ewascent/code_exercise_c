from tail_recursion import tail_recursive, recurse

#USAGE: if catch_nonint([1,2,3,"x", 5]: raise TypeError("Not all values are ints") )
def assertAllInts(nums):
    """Data validation routine to ensure we are parsing an array of ints"""

    for num in nums:
        _num = str(num).lstrip().rstrip()
        is_good = None
        if isinstance(num, int) and is_good != False:
            is_good = True
        else:
            is_good = False
            return is_good
    return is_good

"""
OLD FUNCTION FOR REFERENCE
#USAGE x = repeater([1,2,3]; print(str(x) + " is the first repeated int"))
def repeater(nums):
    val = None

    if not assertAllInts(nums):
        raise TypeError("Not all values are ints in:" + str(nums))

    for index in range(0, len(nums)):
        curr = int(str(nums[index]).lstrip().rstrip())
        for new_index in range ((index + 1), len(nums)):
            if nums[new_index] == nums[index]:
                val = nums[index]
                return val
    return None
"""

#if you use this fancy decorator, you actually ruin native recursions
#but I put a bunch of effort in researching this so feel free to try it
#@tail_recursive
def repeater_tail_recurse(nums, val = None, accum = 0):
    """Recurse over the array of ints and find the first match. Sorts the list to slightly optimize matching"""
    # data validation one time only
    if accum == 0:
        if not assertAllInts(nums):
            raise TypeError("Not all values are ints in:" + str(nums))
        nums = sorted(nums) # change liklyhood of this being a worst case matching scenario

    # get the current value to validate, clean it a bit
    curr = int(str(nums[accum]).lstrip().rstrip())

    # increment the accumulator, skipping the current vals index
    accum = accum + 1

    # remove from O(n2) to O(N+n)
    for index in range (accum, len(nums)):
        if nums[index] == curr:
            val = nums[accum]
            return val

    # recurse if there is more thasn one element left to compare
    # noting accumulator starts at zero
    if len(nums) > accum :
        return repeater_tail_recurse(nums, val, accum + 1)
    return val
