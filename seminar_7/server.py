import socket

server = socket.socket()            # создаем объект сокета сервера
# hostname = socket.gethostname()     # получаем имя хоста локальной машины
port = 12345                        # устанавливаем порт сервера
server.bind(('127.0.1.1', port))       # привязываем сокет сервера к хосту и порту
# начинаем прослушиваение входящих подключений
server.listen(5)

print(server)
print("Server starts")

con, addr = server.accept()     # принимаем клиента
print("connection: ", con)
print("client address: ", addr)

message = "Hello Client!"       # сообщение для отправки клиенту
byteMessage = message.encode()
con.send(byteMessage)      # отправляем сообщение клиенту
data = con.recv(1024)
print(data.decode())
con.close()                     # закрываем подключение

print("Server ends")
server.close()
