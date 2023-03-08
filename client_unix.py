import socket

sock_unix_name = 'unix.sock'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.sendto('Hello World'.encode('utf-8'), sock_unix_name)