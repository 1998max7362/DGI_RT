import socket
from _thread import start_new_thread 

server = socket.socket()

server.bind(('localhost', 3000))

server.listen(5)
print('SERVER ',server)


con, addr = server.accept()
message = 'ПРИВЕТ КЛИЕНТ!'
data = message.encode()
con.send(data)
    
def getMessages():
    while True:
        data = con.recv(1024)
        print('Входящее сообщение',data.decode())
        if data.decode() =='Закрывай!':
            break
    con.close()
    server.close()

start_new_thread(getMessages, ())

while True:
    message = input('Введите сообщение: ')
    data = message.encode()
    con.send(data)
    if message =='Закрывай!':
        break


con.close()
server.close()