import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8888))

message = input('Введите сообщение на сервер: ').strip()
sock.send(message.encode('utf-8'))
sock.close()