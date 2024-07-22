
# import socket
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('192.168.1.197', 9897))
# server.listen()
#
# while True:
#     client, address = server.accept()
#     message = client.recv(1024).decode('utf-8')
#     if message == 'quit':
#         flag = False
#     else:
#         print(message)
#     client.send(input('Server:').encode('utf-8'))
#
# client.close()
# server.close()

