import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 5555))

servidor.listen()
cliente, end = servidor.accept()

terminado = False

while not terminado:
    msg = cliente.recv(1024).decode('utf-8')
    if msg =='encerrar':
        terminado = True
    else:
        print(msg)
    cliente.send(input('mensagem: ').encode('utf-8'))

cliente.close()
servidor.close()