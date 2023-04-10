from socket import *

def resData(filename):
    if '.html' in filename :
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html'
    elif '.png' in filename:
        f = open(filename, 'rb')
        mimeType = 'image/png'
    elif '.ico' in filename:
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'
    elif filename == 'err':
        resHeader = 'HTTP/1.1 404 Not Found\r\n'+'\r\n'
        resBody = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'+'<BODY>Not Found</BODY></HTML>'
        return resHeader,resBody
    else:
        return -1
    resBody = f.read()
    resHeader = 'HTTP/1.1 200 OK\r\n'+'Content-Type: '+mimeType+'\r\n'+'\r\n'
    f.close()
    return resHeader,resBody

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    filename = req[0].split()[1][1:]
    
    if 'index.html' == filename:
        resHeader,resBody = resData(filename)
        c.send(resHeader.encode())
        c.send(resBody.encode('euc-kr'))
    elif 'iot.png' == filename:
        resHeader,resBody = resData(filename)
        c.send(resHeader.encode())
        c.send(resBody)
    elif 'favicon.ico' == filename:
        resHeader,resBody = resData(filename)
        c.send(resHeader.encode())
        c.send(resBody)
    else:
        resHeader,resBody = resData('err')
        c.send(resHeader.encode())
        c.send(resBody.encode())
    c.close()