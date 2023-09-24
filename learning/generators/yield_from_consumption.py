"""The highlighted code is an example of using the yield from statement in Python.
The yield from statement is used to delegate to another generator or iterable.
In this case, the merge function takes two iterables x and y, and yields all the elements
from x and y using the yield from statement.

The for loop then iterates over the merged result of four iterables:
[1, 2, 3], [4, 5, 6], [7, 8, 9], and [10, 11, 12]. The print statement
then prints each element of the merged result on a new line."""


def merge(x, y):
    yield from x
    yield from y


def flatten(lst):
    for sublist in lst:
        if isinstance(sublist, list):
            yield from flatten(sublist)
        else:
            yield sublist


if __name__ == '__main__':
    print("Merging \n")
    for i in merge(
        merge([1, 2, 3],
              [4, 5, 6]),
        merge([7, 8, 9],
              [10, 11, 12])):
        print(i)

    print("\nFlattening \n")
    for i in flatten([1, 2, 3, [4, 5, 6], 7, 8, 9, [10, 11, 12]]):
        print(i)
