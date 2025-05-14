from socket import *
import sys

if len(sys.argv) != 4:
    print("Usage: client.py <server_host> <server_port> <filename>")
    sys.exit(1)

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]

try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.settimeout(5)
    clientSocket.connect((serverName, serverPort))

    requestMessage = f"GET /{filename} HTTP/1.1\r\nHost: {serverName}\r\n\r\n"
    clientSocket.send(requestMessage.encode())

    responseMessage = b""
    while True:
        buffer = clientSocket.recv(4096)
        if not buffer:
            break
        responseMessage += buffer

    print(responseMessage.decode(errors='replace'))
    clientSocket.close()

except timeout:
    print(f"Error: Server at {serverName}:{serverPort} did not respond within timeout period.")
except ConnectionRefusedError:
    print(f"Error: Unable to connect to the server at {serverName}:{serverPort}.\n"
          "Please check if the server is running and the port is correct.")
except Exception as e:
    print(f"Error: {e}")