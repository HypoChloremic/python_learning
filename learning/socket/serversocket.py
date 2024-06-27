# server socket

import socket
 
def Main():
    host = "127.0.0.1"
    port = 5000
    # This creates the socket, seemingly we are not 
    # parsing in any arguments, which will be seen in other examples. 
    mySocket = socket.socket()

	# This binds the socket to the host and port, which 
	# dedicates the socket to that host and port.
    mySocket.bind((host,port))
    
    # listen means that mysocket will start listening for shit, 
    # if we use 1, it means it will listen into perpetuity. 
    # this is ofc unique to the server, because the server
    # is waiting for shit to talk to it. 

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
    		# recv takes a buffer size, which is a region in memory and dedicates
    		# it to what will be received fromm conn. 
            data = conn.recv(1024).decode() # recv takes a 
            if not data:
                    break
            print ("from connected  user: " + str(data))
             
            data = str(data).upper()
            print ("sending: " + str(data))
            conn.send(data.encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()