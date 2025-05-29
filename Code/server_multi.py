from socket import *
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((SERVER_HOST, SERVER_PORT))
serverSocket.listen(5)

def handle_client_multi(connectionSocket, addr):
    print(f"Connection from {addr}")

    try:
        while True:
            message = connectionSocket.recv(1024).decode(errors='replace')
            if not message:
                break

            print(f"Request from {addr}:\n{message}")

            if "exit" in message.lower():
                print(f"Client {addr} requested to end the session.")
                break

            try:
                filename = message.split()[1].lstrip('/')
                if '..' in filename or filename.startswith('/'):
                    header = "HTTP/1.1 403 Forbidden\r\nContent-Type: text/html\r\n\r\n"
                    body = "<html><body><h1>403 Forbidden</h1></body></html>"
                    connectionSocket.send(header.encode())
                    connectionSocket.send(body.encode())
                    continue

                with open(filename, encoding='utf-8') as f:
                    content = f.read()

                header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
                connectionSocket.send(header.encode())
                connectionSocket.sendall(content.encode())

            except FileNotFoundError:
                header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
                body = "<html><body><h1>404 Not Found</h1></body></html>"
                connectionSocket.send(header.encode())
                connectionSocket.send(body.encode())
            except (IndexError, IOError):
                continue

    except Exception as e:
        print(f"Error with client {addr}: {e}")
    
    connectionSocket.close()
    print(f"Connection with {addr} closed.\n")

while True:
    connectionSocket, addr = serverSocket.accept()
    thread = threading.Thread(target=handle_client_multi, args=(connectionSocket, addr))
    thread.start()

"""
Saat ini, server web hanya menangani satu request HTTP pada satu waktu. Implementasikan 
sebuah server multithread yang mampu melayani beberapa requests secara simultan. Dengan 
menggunakan  threading,  pertama-tama  buat  sebuah  thread  utama  di  mana  server  yang 
dimodifikasi listens klien pada port tertentu. Ketika menerima request koneksi TCP dari 
seorang  klien,  server  akan  menyiapkan  koneksi  TCP  melalui  port  lain  dan  melayani 
permintaan klien dalam sebuah thread terpisah. Akan ada sebuah koneksi TCP terpisah dalam 
sebuah utas terpisah untuk setiap pasangan permintaan/respons.
"""