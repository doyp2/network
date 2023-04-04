import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)

sock.connect(addr)

while True:
    msg = input('Q: ')
    try:
        sock.send(msg.encode())
        if msg == 'q':
            break
    except:
        break

    try:
        data = sock.recv(1024)
    except:
        break
    else:
        if not data:
            break
        print('A:',data.decode())

sock.close()