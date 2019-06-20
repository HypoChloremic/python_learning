"""
This file seeks to explain the different functions
associated with lists, and therefore arrays.

SLICING:

Let us create a list:
Z = [1,2,3,4]

The index of the first element is zero, and the last is
three.

If we write Z[1], then python will spit 2 out.
If we write Z[2], then python will spit 3 out.

With lists, the following is also associated:
Z[start:end:step]

Z[start (which is some integer): (this colon is important)] Python will
spit out the elements from the index int(start) to the end.

Z[start:end] python will spit out the elements from index start to one before
end (with other words, int(end)-1)

Z[:end] will spit out from index zero to index int(end)-1

Z[-1] is the last item of the array (Z[-1] = 4 in this case)

Z[:-1] everything but not including the last item.
Z[:-2] everythin but not including the last two items.
"""
