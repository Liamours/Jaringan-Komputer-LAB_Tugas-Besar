# Import socket module
from socket import *
import sys # In order to terminate the program

# Create a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# Fill in start
SERVER_PORT = 1234 # Port number for the server
serverSocket.bind(('127.0.0.1', SERVER_PORT)) # Bind the socket to the port
serverSocket.listen(5) # Listen for incoming connections
# Fill in end

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]

        # Open file with utf-8 encoding
        f = open(filename[1:], encoding='utf-8')
        outputdata = f.readlines()

        # Send HTTP header
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())

        # Send file contents
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send 404 error message
        connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close()

serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data