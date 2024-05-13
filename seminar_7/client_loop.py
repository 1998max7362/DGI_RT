import socket
import time

client = socket.socket()            # создаем сокет клиента
# hostname = socket.gethostname()     # получаем хост сервера
port = 12345                        # устанавливаем порт сервера
client.connect(('localhosttt', 12345))    # подключаемся к серверу
data = client.recv(1024)            # получаем данные с сервера
print("Server sent: ", data.decode())    # выводим данные на консоль

while True:
  message = input('Введите сообщение: ')
  binaryMessage = message.encode()
  client.send(binaryMessage)
client.close()                      # закрываем подключение
