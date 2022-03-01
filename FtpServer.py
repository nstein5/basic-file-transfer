import socket                   # Import socket module
import os
port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
s.bind(("127.0.0.1", port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
c, addr = s.accept()
print("Got a connection from ", addr)
while True:
    dnfilesz = c.recv(1024).decode("utf-8")
    ############################################
    print(dnfilesz)
    dnfilesz = 1#int(dnfilesz)
    dfile = c.recv(1024)
    dfile = dfile.decode("utf-8")
    with open(f'E://test/{dfile}', 'wb') as f:
        #print('file opened')
        dnfilesz = dnfilesz/1024
        #print(dnfilesz)
        yessir = 0
        while (yessir < dnfilesz):
            data = c.recv(1024)
            if not data:
                break
            f.write(data)
            yessir = yessir + 1
            f.close()
            break
    f.close()
