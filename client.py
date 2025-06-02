from socket import *
import sys

if len(sys.argv) != 3:
    print("Penggunaan: <client.py> <server_host> <server_port>")
    sys.exit(1)

server_host = sys.argv[1]
server_port = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server_host, server_port))
print(f"Terhubung dengan {server_host}:{server_port}")

while True:
    filename = input("Isi nama file (atau 'exit'): ").strip()
    if not filename:
        continue
    if filename.lower() == "exit":
        break
    
    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    clientSocket.send(request.encode())
    
    response = clientSocket.recv(4096).decode()
    print(response)

clientSocket.close()

"""
Daripada menggunakan browser, tulislah klien HTTP sendiri untuk menguji server. Klien akan 
terhubung ke server menggunakan koneksi TCP, mengirimkan permintaan HTTP ke server, 
dan menampilkan respons server sebagai output. Asumsikan bahwa request HTTP yang sent 
adalah metode GET. 

Klien harus menerima argumen baris perintah yang menentukan alamat IP server atau nama 
host, port di mana server mendengarkan, dan jalur di mana objek yang diminta disimpan di 
server. Berikut adalah format perintah masukan untuk menjalankan klien.  

client.py server_host server_port filename
"""