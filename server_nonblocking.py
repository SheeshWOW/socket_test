import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8888))
sock.listen(5)
#sock.setblocking(False)
sock.settimeout(5)

while True:
    try:
        client, addr = sock.accept()
    except socket.error:
        print('No clients now')
    except KeyboardInterrupt:
        break
    else:
        client.setblocking(True)
        result = client.recv(1024)
        client.close()
        print(f'{addr}:', result.decode('utf-8'))