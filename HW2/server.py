import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('',9000))
sock.listen(2)

client, addr = sock.accept()

print('Connetion from', addr)
client.send(b'hello '+ addr[0].encode())

name = client.recv(1024) # 이름 출력
print(name.decode())
client.send(b'20181505') # 학번 전송

client.close()