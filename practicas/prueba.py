
import random
import struct

floatlist = [random.random() for _ in range(10)]
buf = struct.pack('%sd' % len(floatlist), *floatlist)
unp = struct.unpack('%sd' % len(floatlist), buf)
print(unp)
print(len(buf)/8)
print(len(floatlist))