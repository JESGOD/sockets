
# socket cliente
import socket
with  socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketCliente:
    socketCliente.connect(('127.0.0.1', 9191))
    print('conexion establecida con el servidor')
    #------------------------intercambio de informacion -----------------------
    socketCliente.sendall('hola servidor soy el cliente'.encode())
    print('acabo de saludar al servidor, ahora voy a resibir lo que ne responda el servidor')
    #----- 1020 maximo de memoria utilizada para resibir datos
    respuesta = socketCliente.recv(1024).decode()
    print('resibi datos del servidor', respuesta)