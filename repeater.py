#USAGE: if catch_nonint([1,2,3,"x", 5]:)
def assertAllInts(nums):

    for num in nums:
        _num = str(num).lstrip().rstrip()
        isGood = None
        if isinstance(num, int) and isGood != False:
            isGood = True
        else:
            isGood = False
            return isGood
    return isGood

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
