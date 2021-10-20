"""
find sum of squared even values in the following list
"""
from functools import reduce

values = [4, 8, 15, 16, 23, 42]
total = 0
for value in values:  # outer loop
    if value % 2 == 0:
        squared = value * value
        total = total + squared
print(total)


def is_even(n):
    return n % 2 == 0


def square(x):
    return x * x


def topla(x, y):
    return x + y


# one-liner
print(reduce(topla, map(square, filter(is_even, values)), 0))

gun = lambda u, v: u + v

print(reduce(gun, map(lambda z: z * z, filter(lambda x: x % 2 == 0, values)), 0))
