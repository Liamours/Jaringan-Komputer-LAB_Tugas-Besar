from socket import *

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((SERVER_HOST, SERVER_PORT))
serverSocket.listen(1)

def handle_client(connectionSocket, addr):
    print("Koneksi baru")
    
    try:
        while True:  
            message = connectionSocket.recv(1024).decode().strip()
            if not message or message.lower() == 'exit':
                print("Koneksi client tertutup")
                break
                
            try:
                filename = message.split()[1][1:]  
                with open(filename, encoding='utf-8') as f:
                    content = f.read()
                response = "HTTP/1.1 200 OK\r\n\r\n" + content
                
            except FileNotFoundError:
                response = "HTTP/1.1 404 Not Found\r\n\r\nFile not found"
            except IndexError:
                response = "HTTP/1.1 400 Bad Request\r\n\r\nInvalid request"
                
            connectionSocket.send(response.encode())
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connectionSocket.close()
        print("Koneksi tertutup\n")

while True:
    connectionSocket, addr = serverSocket.accept()
    handle_client(connectionSocket, addr)

"""
Anda akan mengembangkan sebuah server web yang menangani satu request HTTP pada satu 
waktu. Server web harus accept dan parse request HTTP, mendapatkan file yang diminta dari 
sistem file server, membuat message response HTTP yang terdiri dari file yang requested yang 
didahului oleh baris header, dan kemudian send response langsung ke klien. Jika file yang 
diminta tidak ada di server, server harus mengirimkan message HTTP "404 Not Found" 
kembali ke klien.
"""