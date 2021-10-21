numbers = [4, 8, 15, 16, 23, 42]

with open("exercise1.txt", mode="wt") as f:
    for number in numbers:
        f.write(str(number))

with open("exercise1.data", mode="wb") as f:
    for number in numbers:
        f.write(number.to_bytes(6, byteorder="big"))

with open("exercise1.data", mode="rb") as f:
    """ 
               1111111111222222 
     01234567890123456789012345
     |< 4>||< 8>||<15>||<16>|
    """
    f.seek(6*(4-1)) # offset: 18
    x = int.from_bytes(f.read(6), byteorder="big")
    print(x)

with open("exercise1.data", mode="rb") as f:
    # offset: 0
    print(int.from_bytes(f.read(6), byteorder="big"))
    # offset: 6
    print(int.from_bytes(f.read(6), byteorder="big"))
    # offset: 12
    print(int.from_bytes(f.read(6), byteorder="big"))
