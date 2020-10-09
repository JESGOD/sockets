import socket
class Calculadora:

    def suma(self):
        bandera = False
        while bandera == False:
            try:
                print(" ingrese el primer numero ")
                n1 = int(input())
                print(" ingrese el segundo numero ")
                n2 = int(input())
                resultadoS = n1 + n2
                print("***** el resultado de la suma es:", resultadoS, "*****")
                bandera = True
            except ValueError:
                print("\n********** ERRO: por favor ingrese un valor correcto **********\n")

        def resta(self):
            bandera = False
            while bandera == False:
                try:
                    print("ingrese el primer numero")
                    n1 = int(input())
                    print("ingrese el segundo numero")
                    n2 = int(input())
                    resultadoR = n1 - n2
                    print("***** el resultado de la resta es ", resultadoR, "*****")
                    bandera = True
                except ValueError:
                    print("\n********** ERRO: por favor ingrese un valor correcto **********\n")

        def producto(self):
            bandera = False
            while bandera == False:
                try:
                    print("ingrese el primer numero")
                    n1 = int(input())
                    print("ingrese el segundo numero")
                    n2 = int(input())
                    resultadoP = n1 * n2
                    print("***** el resultado de la multiplicacion es ", resultadoP, "*****")
                    bandera = True
                except ValueError:
                    print("\n********** ERRO: por favor ingrese un valor correcto **********\n")

        def division(self):
            bandera = False
            while bandera == False:
                try:

                    print("ingrese el primer numero")
                    n1 = int(input())
                    print("ingrese el segundo numero")
                    n2 = int(input())
                    resultadoD = n1 / n2
                    print("el resultado de la division es ", resultadoD)
                    bandera = True
                except ValueError:
                    print("\n********** ERRO: por favor ingrese un valor correcto **********\n")
                except ZeroDivisionError:
                    print("\n********** ERRO: no se puede dividir por cero **********\n")