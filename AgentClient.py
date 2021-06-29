
# Socket Library
import socket
import string

print(" ")
print("*******************************************************")
print("Welcome! Lets try to guess a number I'm thinking off...")
print("*******************************************************")
print(" ")

#Keep an open loop until the user inputs 'done" which notifies the client and server to shut down
Done = False
while not Done:

	# Set host name and port number
	host = 'local host'
	port = 5005

	# TCP / IP protocol
	# create a socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#connect the socket to server and port (127.0.0.1 used to denote localhost)
	s.connect(('127.0.0.1', port))

	#Ask the user to guess a number
	msg = input("Enter the number (when finished type done): ")

	# if the user inputs 'done', shut down the server then shut down the client
	if (str(msg).lower() == 'done'):
		print("Shutting down client, Goodbye!")
		s.send(str(msg).encode())
		Done = True
	s.send(str(msg).encode())

	# receive message string from
	msg = s.recv(1024)

	# print out the received message
	while msg:
		print('Received from Server: ' + msg.decode())
		msg = s.recv(1024)

# disconnect the socket
	s.close()
