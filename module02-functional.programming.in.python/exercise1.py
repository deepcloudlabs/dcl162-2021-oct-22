"""
   Functional Programming
    i. pure function: sum(), min(), max()
       lambda expression
   ii. higher-order function: filter, map, reduce
       generator function -> yield
"""
values = [4, 8, 15, 16, 23, 42]
print(sum(values))
print(min(values))
print(max(values))


def for_each(numbers, action):  # higher-order function
    for number in numbers:
        action(number)


def prn(u):
    print(u)


for_each(values, prn)
