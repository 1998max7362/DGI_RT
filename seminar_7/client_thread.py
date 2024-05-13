import socket
from _thread import start_new_thread

client = socket.socket()            # создаем сокет клиента
# hostname = socket.gethostname()     # получаем хост сервера
port = 12345                        # устанавливаем порт сервера
client.connect(('localhost', 12345))    # подключаемся к серверу
data = client.recv(1024)            # получаем данные с сервера
print("Server sent: ", data.decode())    # выводим данные на консоль

flag = True

def showMessages():
  while True:
      data = client.recv(1024)
      print(data.decode())
      if data.decode() == 'Пока!':
        break
  
  client.close()
  global flag
  flag = False
  print('Disconnected')

start_new_thread(showMessages, ())

while True:
  message = input()
  if flag:
    binaryMessage = message.encode()
    client.send(binaryMessage)
  else:
    break