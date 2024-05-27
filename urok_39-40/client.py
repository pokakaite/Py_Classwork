import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.194', 9897)) ## айпи сервера
flag = True
while flag:
    client.send(input('Client_2: ').encode('utf-8'))
    message = client.recv(1024).decode('utf-8')
    if message == 'quit':
        flag = False
    else:
        print(message)

client.close()
