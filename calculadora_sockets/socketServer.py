#socket servidor

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketServer:
    socketServer.bind(('127.0.0.1', 9191))
    socketServer.listen()
    print('servidor encendido, esperando conexiones')
    conexion, direccion = socketServer.accept()
   # with conexion:
    print('conexion establecida desde :', direccion)
    while True:
        datosR = conexion.recv(1024).decode()
        if not datosR:
            break
        print('he resibido los datos desde el cliente', datosR)
        conexion.sendall('hola desde el servidor'.encode())
