"""functions used to find the first matching number in an arbitrarily long list"""
from io import BytesIO, BufferedReader, DEFAULT_BUFFER_SIZE
#from tail_recursion import tail_recursive, recurse

def assert_all_ints(reader, nums, buffer_size = DEFAULT_BUFFER_SIZE):
    """Data validation routine to ensure we are parsing an array of intsself.
    USAGE: if catch_nonint([1,2,3,"x", 5]: raise TypeError("Not all values are ints") )"""
    # TODO: BufferedReader or BytesIO?
    # _nums = BytesIO(nums)
    # buffer = _nums.getbuffer()
    if not reader.readable():
        raise IOError("ERROR - argument reader is not readible on evocation.")
    if buffer_size is None:
        raise IOError("ERROR - you passed in an invalid buffer_size argument.")
    _nums = reader(nums, buffer_size)
    # TODO: how to iterate through buffer like this for loop
    for num in _nums:
        _num = str(num).lstrip().rstrip()
        is_good = None
        if isinstance(num, int) and is_good != False:
            is_good = True
        else:
            is_good = False
            return is_good
    return is_good

#if you use this fancy decorator, you actually ruin native recursions
#but I put a bunch of effort in researching this so feel free to try it
#@tail_recursive
def repeater_tail_recurse(nums, val=None, accum=0):
    """Recurse over the array of ints and find the first match.
    Sorts the list to slightly optimize matching"""
    # data validation one time only
    if accum == 0:
        if not assert_all_ints(reader, nums, buffer_size = DEFAULT_BUFFER_SIZE):
            raise TypeError("Not all values are ints in:" + str(nums))
        nums = sorted(nums) # change liklyhood of this being a worst case matching scenario

    # get the current value to validate, clean it a bit
    curr = int(str(nums[accum]).lstrip().rstrip())

    # increment the accumulator, skipping the current vals index
    accum += 1

    # remove from O(n2) to O(N+n)
    for index in range(accum, len(nums)):
        if nums[index] == curr:
            val = nums[accum]
            return val

    # recurse if there is more thasn one element left to compare
    # noting accumulator starts at zero
    if len(nums) > accum:
        return repeater_tail_recurse(nums, val, accum)
    return val
