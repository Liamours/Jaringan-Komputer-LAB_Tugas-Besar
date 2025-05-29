from socket import *
import sys

if len(sys.argv) != 3:
    print("Usage: python client.py <host> <port>")
    sys.exit(1)

server = (sys.argv[1], int(sys.argv[2]))

try:
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(5)
    s.connect(server)
    print("Ketik nama file yang akan dibuka (contoh: '1.html') atau ketik 'exit' untuk keluar dari client.")

    while True:
        name = input("Nama file, atau exit: ").strip()
        if not name:
            continue
        s.send(f"GET /{name} HTTP/1.1\r\nHost: {server[0]}\r\n\r\n".encode())
        if name.lower() == "exit":
            break

        data = b""
        while True:
            try:
                chunk = s.recv(4096)
                if not chunk:
                    break
                data += chunk
            except timeout:
                break

        text = data.decode(errors='replace')
        status, body = (text.split("\r\n\r\n", 1) + [""])[:2]
        print(f"\nStatus: {status.splitlines()[0] if status else 'No response'}")
        print("Body:\n" + body + "\n")

    s.close()
except timeout:
    print(f"Timeout: No response from {server[0]}:{server[1]}")
except ConnectionRefusedError:
    print(f"Connection refused by {server[0]}:{server[1]}")
except Exception as e:
    print(f"Error: {e}")

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