import socket
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

client, addr = server.accept()
data = client.recv(1024)

first, last, age, gender, occupation, weight = struct.unpack("10s 10s i s 15s f", data)

print(first.decode())
print(last.decode())
print(age)
print(gender.decode())
print(occupation.decode())
print(round(weight, 2))
