from util.exercise1 import Time  # import class

time1 = Time(10, 51, 20)  # Time -> object

# object -> attribute/property -> read
print(f'{time1.hour}h:{time1.minute}m:{time1.second}s')
time1.minute = 23  # write
# time1.second = 45  # Error: read-only attribute
print(f'{time1.hour}h:{time1.minute}m:{time1.second}s')
print(time1)
print(str(time1))
print(time1.__dict__)
print(time1.__dict__['_hour'])
print(time1.__dict__['_minute'])
first, second, *rest = time1.__dict__
print(first, second)