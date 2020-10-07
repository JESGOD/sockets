#socket Servidor
from Calculadora import Calculadora
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketServer:
    socketServer.bind(('127.0.0.1', 9191))
    socketServer.listen()
    print('servidor encendido, esperando conexiones')
    conexion, direccion = socketServer.accept()
   # with conexion:
    print('conexion establecida desde :', direccion)
    while True:
        conexion.sendall("  por favor ingrese una opcion:\n"
                         "          1: sumar \n"
                         "          2: restar \n"
                         "          3: multiplicar \n"
                         "          4: dividir \n"
                         "          5: salir \n".encode())
        datosR = conexion.recv(1024).decode()
        calculadora1 = Calculadora()
        if not datosR:
            break
        opcion = int(input())
        if datosR == 1:
            calculadora1.suma()
        elif datosR == 2:
            calculadora1.resta()

        elif datosR == 3:
            calculadora1.producto()
        else:
            if datosR == 4:
                calculadora1.division()


