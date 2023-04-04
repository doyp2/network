import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)

sock.connect(addr)

while True:
    msg = input()
    try:
        sock.send(msg.encode())
        if msg == 'q':
            break
    except:
        break

sock.close()