
# socket Cliente
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketCliente:

    socketCliente.connect(('127.0.0.1', 9292))
    print('conexion establecida con el servidor')

    # intercambio de informacion

    # -resibe menu desde el servidor y lo imprime
    respuestaMenu = socketCliente.recv(1024).decode()
    print(respuestaMenu,"\n")
    # resibe desde teclado la opcion de menu y la envia
    envio = input().encode()
    socketCliente.sendall(envio)

    # intercambio de datos para las operacioens


    # resibe (ingrese el primer numero) - imprime el mensaje y envia el dato
    respuestaNum1 = socketCliente.recv(1024).decode()
    print(respuestaNum1)
    n1 = input()
    socketCliente.sendall(n1.encode())
    # resibe (ingrese el segundo numero) - imprime el mensaje y envia el dato
    respuestaNum2 = socketCliente.recv(1024).decode()
    print(respuestaNum2)
    n2 = input()
    socketCliente.sendall(n2.encode())

    # resibe el resultado y lo muestra
    respuesta = socketCliente.recv(1024).decode()
    print(respuesta, "\n" )
    respuestaResult = socketCliente.recv(1024).decode()
    print("          ",respuestaResult)

