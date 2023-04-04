import socket

op = ['+','-','*','/']

def calculator(s):
    for i in range(len(op)):
        if op[i] in s:
            a,b = map(int,s.split(op[i]))
            if op[i] == '+':
                return a+b
            elif op[i] == '-':
                return a-b
            elif op[i] == '*':
                return a*b
            else:
                return round(a/b,1)
    return 'input error'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('',9000))
sock.listen(1)

client, addr = sock.accept()

while True:
    try:
        data = client.recv(1024)
    except:
        break
    else:
        if not data:
            break
        msg = data.decode()
        print('recv:',msg)
        if msg == 'q':
            break

    try:
        client.send(str(calculator(msg)).encode())
        print('send:',calculator(msg))
    except:
        break
        
sock.close()