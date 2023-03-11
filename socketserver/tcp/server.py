import socketserver

class socketTCPServer(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        addr_ip = self.client_address[0]

        print(data, addr_ip)


if __name__ == "__main__":
    with socketserver.TCPServer(('', 8888), socketTCPServer) as server:
        server.serve_forever()