from functools import reduce

values = [4, 8, 15, 16, 23, 42]


def is_even(n):
    print(f"is_even({n})")
    return n % 2 == 0


def square(x):
    print(f"square({x})")
    return x * x


def topla(x, y):
    print(f"topla({x},{y})")
    return x + y


print(reduce(topla, map(square, filter(is_even, values)), 0))