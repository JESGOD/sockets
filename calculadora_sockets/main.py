
# socket Cliente
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketCliente:

    socketCliente.connect(('127.0.0.1', 9292))
    print('conexion establecida con el servidor')

    # intercambio de informacion

    # resibe menu desde el servidor y lo imprime
    while True:
        respuestaMenu = socketCliente.recv(1024).decode()
        if not respuestaMenu:
            break
        print(respuestaMenu,"\n")
        # resibe desde teclado la opcion de menu y la envia
        envioM = input().encode()
       # if not envioM:
        #    break
        socketCliente.sendall(envioM)



