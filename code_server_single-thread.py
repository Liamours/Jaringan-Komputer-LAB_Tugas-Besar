import socket
import os
import threading

class SimpleWebServer:
    def __init__(self, host='', port=6789):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"Server berjalan di http://{self.host or 'localhost'}:{self.port}")
        
        while True:
            client_connection, client_address = self.server_socket.accept()
            print(f"Koneksi dari: {client_address}")
            self.handle_request(client_connection)
            client_connection.close()
    
    def handle_request(self, client_connection):
        request = client_connection.recv(1024).decode()
        print(f"Request:\n{request}")
        
        headers = request.split('\n')
        if not headers:
            self.send_response(client_connection, 400, "Bad Request")
            return
            
        method, path, _ = headers[0].split()
        if method != 'GET':
            self.send_response(client_connection, 501, "Not Implemented")
            return
            
        if path == '/':
            path = '/index.html'
            
        try:
            if '..' in path or path.startswith('/'):
                path = path.lstrip('/')
                if not path:
                    path = 'index.html'
                    
            with open(path, 'rb') as file:
                content = file.read()
            self.send_response(client_connection, 200, "OK", content)
        except FileNotFoundError:
            self.send_response(client_connection, 404, "Not Found", b"<h1>404 Not Found</h1>")
        except Exception as e:
            print(f"Error: {e}")
            self.send_response(client_connection, 500, "Internal Server Error", b"<h1>500 Server Error</h1>")
    
    def send_response(self, client_connection, status_code, status_message, content=b""):
        response = f"HTTP/1.1 {status_code} {status_message}\r\n"
        response += "Content-Type: text/html\r\n"
        response += f"Content-Length: {len(content)}\r\n"
        response += "\r\n"
        client_connection.send(response.encode() + content)
    
    def stop(self):
        self.server_socket.close()

if __name__ == "__main__":
    server = SimpleWebServer()
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
        print("\nServer dihentikan")