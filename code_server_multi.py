"""
Saat ini, server web hanya menangani satu request HTTP pada satu waktu. Implementasikan 
sebuah server multithread yang mampu melayani beberapa requests secara simultan. Dengan 
menggunakan  threading,  pertama-tama  buat  sebuah  thread  utama  di  mana  server  yang 
dimodifikasi listens klien pada port tertentu. Ketika menerima request koneksi TCP dari 
seorang  klien,  server  akan  menyiapkan  koneksi  TCP  melalui  port  lain  dan  melayani 
permintaan klien dalam sebuah thread terpisah. Akan ada sebuah koneksi TCP terpisah dalam 
sebuah utas terpisah untuk setiap pasangan permintaan/respons.
"""

from socket import *
import threading
import os

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((SERVER_HOST, SERVER_PORT))
serverSocket.listen(5)

def handle_client(connectionSocket):
    try:
        data = connectionSocket.recv(1024)
        message = data.decode('utf-8', errors='ignore')

        if not message.strip():
            connectionSocket.close()
            return

        parts = message.split()
        if len(parts) < 2:
            connectionSocket.close()
            return

        filename = parts[1]

        if '\x00' in filename:
            connectionSocket.close()
            return

        filename = filename.lstrip('/')
        if '..' in filename or filename.startswith('/'):
            connectionSocket.send("HTTP/1.1 403 Forbidden\r\n\r\n".encode())
            connectionSocket.close()
            return

        if not os.path.exists(filename):
            raise IOError

        with open(filename, encoding='utf-8') as f:
            outputdata = f.read()

        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())

        connectionSocket.sendall(outputdata.encode())

    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())
    finally:
        connectionSocket.close()

print("Multithreaded server is ready to serve...")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
    client_thread.start()