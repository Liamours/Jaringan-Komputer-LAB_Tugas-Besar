from socket import *
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((SERVER_HOST, SERVER_PORT))
serverSocket.listen(5)

def handle_client(connectionSocket, addr):
    print("Terhubung dengan ", addr)

    try:
        while True:
            message = connectionSocket.recv(1024).decode().strip()
            if message == 'exit':
                print("Koneksi client tertutup")
                break

            try:
                filename = message.split()[1][1:]
                with open(filename, encoding='utf-8') as f:
                    content = f.read()
                response = "HTTP/1.1 200 OK\r\n\r\n" + content

            except FileNotFoundError:
                response = "HTTP/1.1 404 Not Found\r\n\r\n"

            connectionSocket.send(response.encode())
            
    except Exception as e:
        print(f"Error: {e}")

    finally:
        connectionSocket.close()
        print("Koneksi tertutup")

while True:
    connectionSocket, addr = serverSocket.accept()
    thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
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