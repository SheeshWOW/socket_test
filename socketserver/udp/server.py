import socketserver


class serverUDPSocket(socketserver.BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        print(f"Data: {data.decode('utf-8')}")
        print(f"Address: {self.client_address[0]}")


if __name__ == '__main__':
    with socketserver.UDPServer(('', 8888), serverUDPSocket) as server:
        server.serve_forever()