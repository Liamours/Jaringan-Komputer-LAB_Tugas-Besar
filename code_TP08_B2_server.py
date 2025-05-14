from socket import *
import sys
import threading # Import threading module

# Function to handle each client request
def handle_client(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode() # Receive the HTTP request
        filename = message.split()[1] # Extract the file name
        f = open(filename[1:], encoding='utf-8')  # Open the requested file
        outputdata = f.read() # Read the content of the file

        # Send HTTP response header
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the file
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close() # Close the connection

    except IOError:
        # Send 404 Not Found response
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html> <head> </head> <body> <h1> 404 Not Found </h1> </body> </html> \r\n".encode())
        connectionSocket.close() # Close the connection

# Main server setup
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 6789)) # Bind to port 6789
serverSocket.listen(5) # Allow up to 5 queued connections

print("Multithreaded server is ready to serve...")

while True:
    # Accept a connection and create a new thread to handle it
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
    client_thread.start() # Start the thread

serverSocket.close()
sys.exit()