
# socket Cliente
import socket
with  socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketCliente:
    socketCliente.connect(('127.0.0.1', 9191))
   # socketCliente.connect(('127.0.0.1', 9090))
    print('conexion establecida con el servidor')
    #------------------------intercambio de informacion -----------------------
    # menu desde el servidor
    respuesta = socketCliente.recv(1024).decode()
    print(respuesta)
    # envio opcion de menu
    socketCliente.sendall(input().encode())



