from socket import *
import sys

if len(sys.argv) != 3:
    print("Penggunaan: <client.py> <server_host> <server_port>")
    sys.exit(1)

SERVER_HOST = sys.argv[1]
SERVER_PORT = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(10)

try:
    clientSocket.connect((SERVER_HOST, SERVER_PORT))
    print("Terhubung dengan Server")
    
    while True:
        filename = input("Isi nama file (atau 'exit'): ")

        if not filename:
            continue
        if filename == "exit":
            break
        
        request = f"GET /{filename} HTTP/1.0\r\nHost: {SERVER_HOST}\r\n\r\n"
        clientSocket.send(request.encode())

        response = ""
        while True:
            try:
                chunk = clientSocket.recv(4096).decode()
                if not chunk:
                    break
                response += chunk
            except timeout:
                break

        print(response)

except Exception as e:
    print(f"Error: {e}")

finally:
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