import socket
import time

client = socket.socket()            # создаем сокет клиента
# hostname = socket.gethostname()     # получаем хост сервера
port = 12345                        # устанавливаем порт сервера
client.connect(('127.0.1.1', 12345))    # подключаемся к серверу
data = client.recv(1024)            # получаем данные с сервера
print("Server sent: ", data.decode())    # выводим данные на консоль
client.send('Сообщение 1'.encode())
client.close()                      # закрываем подключение
