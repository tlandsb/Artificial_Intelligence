#Libraries
import socket
import time

#Keep an open loop until the client sends 'done" which notifies the server to shut down
Done = False
while not Done:

    # Set host name and port number
    host = 'local host'
    port = 5005

    # TCP / IP protocol
    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket with server
    # and port number
    s.bind(('', port))

    # 1 connection allowed to the socket
    s.listen(10)
    print("Server is listening")

    # wait until a connection is accepted
    c, addr = s.accept()

    #Get the string input from the client
    msg2 = c.recv(1024)
    print("The number I received is:", msg2.decode())
    print("Analyzing client data...")
    time.sleep(1)
    print("Analyzing client data...")
    time.sleep(1)
    print("Analyzing client data...")
    time.sleep(1)

    # display client address
    print("CONNECTION FROM:", str(addr))

    # Decode the string from the client... see if its the number exected - if its not send back a hint to let the user know if they
    # need to go up or down in their guess
    if (msg2.decode().lower() == "done"):
        Done = True
        print("Shutting down Server, Goodbye!")
    elif (msg2.decode() == '57'):
        msg = "You got it"
    elif (msg2.decode() > '57'):
        msg = "Wrong number, try going down"
    elif (msg2.decode() < '57'):
        msg = "Wrong number, try going up"

    c.send(msg.encode())

    # disconnect the server
    c.close()
