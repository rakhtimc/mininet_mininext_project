import socket

# next create a socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "Socket successfully created at h1 server"

bind_ip = '0.0.0.0'
port = 1075

s.bind((bind_ip, port))

# put the socket into listening mode
s.settimeout(5)
s.listen(1)
print "socket is listening"

# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print 'Got connection from', addr
    
    f = open('r4.txt','wb')
       
    l = c.recv(1024)
    
    while (l):
        print "Receiving..."
        f.write(l)
        l = c.recv(1024)
    f.close()
    print "Done Receivin"

    # send a thank you message to the client.
    c.send('Thank you for connecting to server')

    # Close the connection with the client
    c.close()
s.close()