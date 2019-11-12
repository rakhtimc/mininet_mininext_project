import socket

# next create a socket object
s_h1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_r2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "Socket successfully created at h1 server"

bind_ip = '0.0.0.0'
port_h1 = 1095
port_r2 = 1096
s_h1.bind((bind_ip, port_h1))
s_r2.bind((bind_ip, port_r2))

# put the socket into listening mode
s_h1.settimeout(30)
s_h1.listen(1)

s_r2.settimeout(30)
s_r2.listen(1)


print "socket is listening"
# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c_h1, addr_h1 = s_h1.accept()
    print 'Got connection from', addr_h1
    
    c_r2, addr_r2 = s_r2.accept()
    print 'Got connection from', addr_r2
        
    f_h1 = open('r1.txt','wb')
    f_r2 = open('r4.txt','wb')

    l_h1 = c_h1.recv(1024)
    l_r2 = c_r2.recv(1024)

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
    
    print "Done Receivin"

    # send a thank you message to the client.
    c_h1.send('Thank you for connecting to server')
    c_r2.send('Thank you for connecting to server')
   
    # Close the connection with the client
    c_h1.close()
    c_r2.close()
   
s_h1.close()
s_r2.close()