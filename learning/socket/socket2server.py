import socket
# import Thread


def server(address):
	sock = socket.socket()
	# sock.setsockopt(socket.socket.SOL_SOCKET, socket.socket.SO_REUSEADDR, 1)
	sock.bind(address)
	sock.listen(5)
	while True:
# Accept a connection. The socket must be bound to an address and 
# listening for connections. The return value is a pair (conn, address) 
# where conn is a new socket object usable to send 
# and receive data on the connection, and address is the address bound
# to the socket on the other end of the connection.
		client, addr = sock.accept()
		print("Connection ", addr)
		handler(client)

def handler(client): # goes into a loop and a request comes accross
	while True:
		req = client.recv(1024)
		if not req:
			break
		try:
			n = int(req)
			result = n**2
			resp = str(result).encode("ascii")+b'\n'
			client.send(resp)
		except ValueError:
			resp = "incorrect".encode("ascii")+b'\n'
			client.send(resp)
	print("Closed")

server(("", 25000))