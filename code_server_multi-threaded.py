import socket
import os
import threading

class MultiThreadedWebServer:
    def __init__(self, host='', port=6789):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Multithreaded server berjalan di http://{self.host or 'localhost'}:{self.port}")
        
        try:
            while True:
                client_connection, client_address = self.server_socket.accept()
                print(f"Koneksi dari: {client_address}")
                
                thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_connection,)
                )
                thread.daemon = True
                thread.start()
        except KeyboardInterrupt:
            print("\nMenghentikan server...")
        finally:
            self.server_socket.close()
    
    def handle_client(self, client_connection):
        try:
            request = client_connection.recv(1024).decode()
            print(f"Request:\n{request}")
            
            if not request:
                return
                
            headers = request.split('\n')
            method, path, _ = headers[0].split()
            
            if method != 'GET':
                self.send_response(client_connection, 501, "Not Implemented")
                return
                
            if path == '/':
                path = '/index.html'
                
            if '..' in path or path.startswith('/'):
                path = path.lstrip('/')
                if not path:
                    path = 'index.html'
                    
            try:
                with open(path, 'rb') as file:
                    content = file.read()
                self.send_response(client_connection, 200, "OK", content)
            except FileNotFoundError:
                self.send_response(client_connection, 404, "Not Found", b"<h1>404 Not Found</h1>")
            except Exception as e:
                print(f"Error: {e}")
                self.send_response(client_connection, 500, "Internal Server Error", b"<h1>500 Server Error</h1>")
        finally:
            client_connection.close()
    
    def send_response(self, client_connection, status_code, status_message, content=b""):
        response = f"HTTP/1.1 {status_code} {status_message}\r\n"
        response += "Content-Type: text/html\r\n"
        response += f"Content-Length: {len(content)}\r\n"
        response += "\r\n"
        client_connection.send(response.encode() + content)

if __name__ == "__main__":
    server = MultiThreadedWebServer()
    server.start()