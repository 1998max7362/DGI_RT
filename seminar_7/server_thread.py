import socket
from _thread import start_new_thread

server = socket.socket()            # создаем объект сокета сервера
# hostname = socket.gethostname()     # получаем имя хоста локальной машины
port = 12345                        # устанавливаем порт сервера
# привязываем сокет сервера к хосту и порту
server.bind(('localhost', port))
# начинаем прослушиваение входящих подключений
server.listen(1)

print(server)
print("Server starts")

con, addr = server.accept()     # принимаем клиента
print("connection: ", con)
print("client address: ", addr)

def showMessages():
  while True:
      data = con.recv(1024)
      print(data.decode())
      if data.decode() == 'Закрывай!':
        message = "Пока!"       # сообщение для отправки клиенту
        byteMessage = message.encode()
        con.send(byteMessage)      # отправляем сообщение клиенту
        break

  con.close()                     # закрываем подключение
  server.close()
  print('Server is closed')

message = "Hello Client!"       # сообщение для отправки клиенту
byteMessage = message.encode()
con.send(byteMessage)      # отправляем сообщение клиенту

start_new_thread(showMessages, ())

while True:
  message = input()
  binaryMessage = message.encode()
  con.send(binaryMessage)

