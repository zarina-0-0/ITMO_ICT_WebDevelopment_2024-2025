import socket

# AF_INET- работать с IP-адресами (IPv4),SOCK_STREAM для протокола TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 8080))
server_socket.listen(1)
print("Сервер запущен на порту 8080...")

while True:
    # Принимаем соединение от клиента
    client_connection, client_address = server_socket.accept()
    print(f'Подключение от {client_address}')

    # Получаем сообщение от клиента
    request = client_connection.recv(1024).decode()
    print(f'Запрос от клиента: {request}')

    # Отправляем ответ клиенту
    response = 'Привет от сервера!'
    client_connection.sendall(response.encode())

    # Закрываем соединение
    client_connection.close()
