# TODO: In progress. No clear way to find from an array w/o reading two streams
"""various forms of stream reading"""
from io import BytesIO, BufferedReader, DEFAULT_BUFFER_SIZE
import numpy as np
import pandas as pd

def assert_all_ints(reader, nums, buffer_size = DEFAULT_BUFFER_SIZE):
    """inject a reader, pass in the array/stream to match on. optionally set a buffer size"""
    # TODO: BufferedReader or BytesIO?
    num_bytes = BytesIO(nums)
    # TODO: do I need a buffer buffer = num_bytes.getbuffer()
    if not reader.readable():
        raise IOError("ERROR - argument reader is not readible on evocation.")
    if buffer_size is None:
        raise IOError("ERROR - you passed in an invalid buffer_size argument.")
    _nums = reader(nums, buffer_size)
    # TODO: how to iterate through buffer like this for loop

def simple_1():
    import re
    data = list(str(range(1, 20)))
    pattern=re.compile(str(3))
    print([m.group(0) for l in data for m in [pattern.search(l)] if m])


def simple_2():
    import re
    data = bytearray(range(1,100))
    dup_data = bytearray(range(0,3))
    data.extend(dup_data)

    with BytesIO(data) as streamer:
    #print(streamer.getvalue())
        base = streamer.read()
        #result = base.find(dup_data)
        result = re.search(int(str(dup_data[1])), base, bytes).group(0)
        print(result)

#def simple():
#    import itertools
#    from operator import itemgetter

#    data = list(range(1,100))
    #final_data = data.extend(list(range(0,3)))

#    for key, group in itertools.groupby(final_data, key=lambda x:x['size']):
#        print(key)
#        print(list(group))

#print(simple())
def merger():
    import heapq
    data = list(range(5,100))
    more_data = list(range(0,6))
    xs = heapq.merge([more_data, data])
    try:
        while xs:
            print(next(xs))
    except StopIteration:
        return None
merger()
