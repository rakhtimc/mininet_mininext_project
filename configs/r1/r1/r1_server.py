import socket

# next create a socket object
s_h1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_r2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_r3 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "Socket successfully created at h1 server"

bind_ip = '0.0.0.0'
port_h1 = 1081
port_r2 = 1082
port_r3 = 1083
s_h1.bind((bind_ip, port_h1))
s_r2.bind((bind_ip, port_r2))
s_r3.bind((bind_ip, port_r3))

# put the socket into listening mode
s_h1.settimeout(30)
s_h1.listen(1)

s_r2.settimeout(30)
s_r2.listen(1)

s_r3.settimeout(30)
s_r3.listen(1)

print "socket is listening"
# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c_h1, addr_h1 = s_h1.accept()
    print 'Got connection from', addr_h1
    
    c_r2, addr_r2 = s_r2.accept()
    print 'Got connection from', addr_r2
    
    c_r3, addr_r3 = s_r3.accept()
    print 'Got connection from', addr_r3

    
    f_h1 = open('h1.txt','wb')
    f_r2 = open('r2.txt','wb')
    f_r3 = open('r3.txt','wb')

    l_h1 = c_h1.recv(1024)
    l_r2 = c_r2.recv(1024)
    l_r3 = c_r3.recv(1024)

    while (l_h1):
        print "Receiving..."
        f_h1.write(l_h1)
        l_h1 = c_h1.recv(1024)
    f_h1.close()
    
    while (l_r2):
        print "Receiving..."
        f_r2.write(l_r2)
        l_r2 = c_r2.recv(1024)
    f_r2.close()
    
    while (l_r3):
        print "Receiving..."
        f_r3.write(l_r3)
        l_r3 = c_r3.recv(1024)
    f_r3.close()

    print "Done Receivin"

    # send a thank you message to the client.
    c_h1.send('Thank you for connecting to server')
    c_r2.send('Thank you for connecting to server')
    c_r3.send('Thank you for connecting to server')

    # Close the connection with the client
    c_h1.close()
    c_r2.close()
    c_r3.close()
s_h1.close()
s_r2.close()
s_r3.close()