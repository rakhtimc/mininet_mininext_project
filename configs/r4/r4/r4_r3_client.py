# Import socket module
import socket

# Create a socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "Socket successfully created at r1 client"

# Define the port on which you want to connect
port = 1099

# connect to the server on local computer
s.connect(('172.0.6.2', port))
print 'connected'

f = open('r4.txt','rb')
print 'Sending start'
l = f.read(1024)

while (l):
    print 'Sending...'
    s.send(l)
    l = f.read(1024)
f.close()
print "Done Sending"
s.shutdown(socket.SHUT_WR)
print s.recv(1024)
s.close                 