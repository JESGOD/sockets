#socket Servidor

import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketServer:
    socketServer.bind(('127.0.0.1', 9292))
    socketServer.listen()
    print('servidor encendido, esperando conexiones')
    conexion, direccion = socketServer.accept()
   # with conexion:
    print('conexion establecida desde :', direccion)
    parseDatosInt = 1
    while parseDatosInt != 5:
        conexion.sendall("  por favor ingrese una opcion:\n"
                             "          1: sumar \n"
                             "          2: restar \n"
                             "          3: multiplicar \n"
                             "          4: dividir \n"
                             "          5: salir \n".encode())
        bandera = True
        while bandera == True:
            try:
                datosR = conexion.recv(1024).decode()
                parseDatosStr = str(datosR)
                print(parseDatosStr)
                parseDatosInt = int(parseDatosStr)
                bandera = False
            except ValueError:
                #control = "1"
                #conexion.sendall(control.encode())
                conexion.sendall("ingrese un valor correcro para el menu".encode())
                parsen1Int = 0

        if parseDatosInt == 1:
            bandera = False
            while bandera == False:
                try:
                    conexion.sendall(" ingrese el primer numero ".encode())
                    n1 = conexion.recv(1024).decode()
                    parsen1Str = str(n1)
                    parsen1Int = int(parsen1Str)

                    conexion.sendall(" ingrese el segundo numero ".encode())
                    n2 = conexion.recv(1024).decode()
                    parsen2Str = str(n2)
                    parsen2Int = int(parsen2Str)
                    resultadoS = parsen1Int + parsen2Int
                    resultadoSCod = str(resultadoS)
                   # conexion.sendall("***** el resultado de la suma es*****".encode())
                    conexion.sendall(resultadoSCod.encode())
                    bandera = True
                except ValueError:
                    print("\n********** ERRO: por favor ingrese un valor correcto **********\n")
        elif parseDatosInt == 2:
            bandera = False
            while bandera == False:
                try:
                    conexion.sendall(" ingrese el primer numero ".encode())
                    n1 = conexion.recv(1024).decode()
                    parsen1Str = str(n1)
                    print(n1)
                    parsen1Int = int(parsen1Str)

                    conexion.sendall(" ingrese el segundo numero ".encode())
                    n2 = conexion.recv(1024).decode()
                    parsen2Str = str(n2)
                    print(parsen2Str)
                    parsen2Int = int(parsen2Str)
                    # print(parsen1Str, "", parsen2Str)
                    resultadoS = parsen1Int - parsen2Int
                    resultadoSCod = str(resultadoS)
                    #conexion.sendall("***** el resultado de la resta es*****".encode())
                    conexion.sendall(resultadoSCod.encode())
                    bandera = True
                except ValueError:
                    print("\n********** ERRO: por favor ingrese un valor correcto **********\n")

        elif parseDatosInt == 3:
            bandera = False
            while bandera == False:
                try:
                    conexion.sendall(" ingrese el primer numero ".encode())
                    n1 = conexion.recv(1024).decode()
                    parsen1Str = str(n1)
                    print(n1)
                    parsen1Int = int(parsen1Str)

                    conexion.sendall(" ingrese el segundo numero ".encode())
                    n2 = conexion.recv(1024).decode()
                    parsen2Str = str(n2)
                    print(parsen2Str)
                    parsen2Int = int(parsen2Str)
                    # print(parsen1Str, "", parsen2Str)
                    resultadoS = parsen1Int * parsen2Int
                    resultadoSCod = str(resultadoS)
                   # conexion.sendall("***** el resultado de la multiplicacion es*****".encode())
                    conexion.sendall(resultadoSCod.encode())
                    bandera = True
                except ValueError:
                    print("\n********** ERRO: por favor ingrese un valor correcto **********\n")
        else:
            if parseDatosInt == 4:
                bandera = False
                while bandera == False:
                    try:
                        conexion.sendall(" ingrese el primer numero ".encode())
                        n1 = conexion.recv(1024).decode()
                        parsen1Str = str(n1)
                        print(n1)
                        parsen1Int = int(parsen1Str)

                        conexion.sendall(" ingrese el segundo numero ".encode())
                        n2 = conexion.recv(1024).decode()
                        parsen2Str = str(n2)
                        print(parsen2Str)
                        parsen2Int = int(parsen2Str)
                        # print(parsen1Str, "", parsen2Str)
                        resultadoS = parsen1Int / parsen2Int
                        resultadoSCod = str(resultadoS)
                       # conexion.sendall("***** el resultado de la division es*****".encode())
                        conexion.sendall(resultadoSCod.encode())
                        bandera = True
                    except ValueError:
                        print("\n********** ERRO: por favor ingrese un valor correcto **********\n")
                    except ZeroDivisionError:
                        print("\n********** ERRO: no se puede dividir por cero **********\n")



