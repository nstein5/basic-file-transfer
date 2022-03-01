import socket                   # Import socket module
import os
s = socket.socket()             # Create a socket object
port = 60000                    # Reserve a port for your service.

s.connect(("127.0.0.0", port))
dfile = input("What file would you like to upload : ")
dfilesz = os.stat(rf"{dfile}")
#print(dfilesz)
#dfilesz =
print(dfilesz)
s.send(str.encode(str(dfilesz.st_size)))
s.send(str.encode(dfile))
dfilesz = dfilesz.st_size
dfilesz = dfilesz/1024
filename=rf"{dfile}"
f = open(filename,'rb')
l = f.read(1024)
yessir = 0
while(yessir < dfilesz):
    s.send(l)
    l = f.read(1024)
    yessir = yessir + 1
    f.close()
    break
