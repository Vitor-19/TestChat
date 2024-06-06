import socket

cliente =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost', 5555))

terminado = False
print('digite encerrar para terminar o chat')

while not terminado:
    cliente.send(input('mensagem: ').encode('utf-8'))
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'encerrar' :
        terminado = True
    else:
        print (msg)
cliente.close()