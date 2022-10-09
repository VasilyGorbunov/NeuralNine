import struct

byte_stream = struct.pack("HHH", 10, 20, 30)
print(byte_stream)

a, b, c = struct.unpack("HHH", byte_stream)
print(a, b, c)
print("-" * 40)

company = b"Tesla"
day, month, year = 5, 9, 2002
awesome = True

byte_stream = struct.pack("5s 3i ?", company, day, month, year, awesome)
print(byte_stream)
print(struct.unpack("5s 3i ?", byte_stream))