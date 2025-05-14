"""
Anda akan mengembangkan sebuah server web yang menangani satu request HTTP pada satu 
waktu. Server web harus accept dan parse request HTTP, mendapatkan file yang diminta dari 
sistem file server, membuat message response HTTP yang terdiri dari file yang requested yang 
didahului oleh baris header, dan kemudian send response langsung ke klien. Jika file yang 
diminta tidak ada di server, server harus mengirimkan message HTTP "404 Not Found" 
kembali ke klien.
"""

from socket import *

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234 
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((SERVER_HOST, SERVER_PORT))
serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode(errors='replace')
        filename = message.split()[1]

        f = open(filename[1:], encoding='utf-8')
        outputdata = f.readlines()

        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close()