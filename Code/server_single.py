from socket import *

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 4321

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((SERVER_HOST, SERVER_PORT))
serverSocket.listen(1)

def handle_client_single(connectionSocket, addr):
    print(f"Connection from {addr}")

    try:
        while True:
            message = connectionSocket.recv(1024).decode(errors='replace')
            if not message:
                break

            print(f"Request from client:\n{message}")

            if "exit" in message.lower():
                print("Client requested to end the session.")
                break

            try:
                filename = message.split()[1].lstrip('/')
                if '..' in filename or filename.startswith('/'):
                    continue

                with open(filename, encoding='utf-8') as f:
                    content = f.read()

                header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
                connectionSocket.send(header.encode())
                connectionSocket.sendall(content.encode())

            except (IndexError, FileNotFoundError, IOError):
                continue

    except Exception as e:
        print(f"Server error: {e}")
    
    connectionSocket.close()
    print(f"Connection from {addr} closed.\n")

print('Single-threaded server is ready to serve...')

while True:
    connectionSocket, addr = serverSocket.accept()
    handle_client_single(connectionSocket, addr)

"""
Anda akan mengembangkan sebuah server web yang menangani satu request HTTP pada satu 
waktu. Server web harus accept dan parse request HTTP, mendapatkan file yang diminta dari 
sistem file server, membuat message response HTTP yang terdiri dari file yang requested yang 
didahului oleh baris header, dan kemudian send response langsung ke klien. Jika file yang 
diminta tidak ada di server, server harus mengirimkan message HTTP "404 Not Found" 
kembali ke klien.
"""