import os
from LISTAS import ListaCarlitos
from PILA import PilaCarlitos
from COLA import ColaCarlitos

class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        while True:
            try:
                opc = input("Hola, por favor escoja una opcion [1..{}]: ".format(len(self.opciones)))
                break
            except ValueError:
                print("Dato erroneo, ingrese un número valido.")
        return opc
opc = ""
while True:
    try:
        tam = int(input("Inserte tamaño de las listas, pilas y colas: "))
        break
    except ValueError:
        print("Dato erroneo, ingrese un número valido.")
pila1 = ListaCarlitos(tam)
lista1 = PilaCarlitos(tam)
cola1 = ColaCarlitos(tam)
while opc != "4":
    os.system("cls")
    men = Menu("*******MENU PRINCIPAl*******",
               ["1)PILA", "2)COLA", "3)LISTA", "4)SALIR"])
    opc = men.menu()
    if opc == "1":
        opc1 =""
        while opc1 != "6":
            os.system("cls")
            men1 = Menu("****MENU PILA****",["1)PUSH","2)POP","3)SHOW","4)LONGITUD","5)EMPTY","6)SALIR"])
            opc1 = men1.menu()
            if opc1 =="1":
                os.system("cls")
                print("*****Insertar un número a la Pila*****")
                for i in range(tam):
                    while True:
                        try:
                            dato = int(input("Inserte el número que desea agregarle a la pila: "))
                            break
                        except ValueError:
                            print("Dato erroneo, ingrese un número valido.")
                    pila1.push(dato)
                    print("Dato ingresado satisfactoriamente.")
                input("Presione una tecla para continuar")
            elif opc1 == "2":
                os.system("cls")
                print("*****Se va a retirar el ultimo digito de la Pila*****")
                while True:
                    try:
                        x = int(input("¿Cuantos elementos quiere quitar de la Pila?: "))
                        break
                    except ValueError:
                        print("Dato erroneo, ingrese un número valido.")
                if x <= tam:
                    for i in range(x):
                        print("El elemento que ha quitado es: {}, correcto?".format(pila1.pop()))
                    input("Presione una tecla para continuar")
                else:
                    print("ERROR, el dato ingresado es un numero mayor al tamaño de la pila o no exite dicha pila.")
                    input("Presione una tecla para continuar")        
            elif opc1 =="3":
                os.system("cls")
                print("*****Muestra los valores de la Pila*****")
                pila1.show()
                input("Presione una tecla para continuar")     
            elif opc1 == "4":
                os.system("cls")
                print("*****Muestra la longitud de la Pila*****")
                print("La longitud de la pila es: {}, correcto?".format(pila1.longitud()))
                input("Presione una tecla para continuar")
            elif opc1 =="5":
                os.system("cls")
                print("*****Demuestra si la Pila esta vacia*****")
                print("<False> para las pilas llenas y <True> para las pila vacias")
                print("---{}---".format(pila1.empty()))
                input("Presione una tecla para continuar")
            elif opc1 =="6":
                print("*****Regresará al menu principal.*****")
                input("Presione una tecla para continuar")
            else:
                print("No es valida")
                input("Presione una tecla para continuar")
                
                
                
                
                
                
                
                
    elif opc == "2":
        opc2 = ""
        while opc2 != "6":
            os.system("cls")
            men2 = Menu("****MENU COLA****", ["1)INSERTAR", "2)QUITAR", "3)MOSTRAR", "4)LONGITUD", "5)EMPTY", "6)SALIR"])
            opc2 = men2.menu()
            if opc2 == "1":
                os.system("cls")
                print("*****Ingreso de un numero a la Cola*****")
                for i in range(tam):
                    dato = int(input("Inserte un numero que desea ingresar a la cola: "))
                    cola1.insertarcarlitos(dato)
                    print("Dato ingresado satisfactoriamente.")
                input("Presione una tecla para continuar")
            elif opc2 == "2":
                os.system("cls")
                print("*****Saca el primer valor de la cola*****")
                x = int(input("¿Cuantos elementos desea quitar a la cola?: "))
                if x <= tam:
                    for i in range(x):
                        print("El elemento quitado es: {}, correcto?".format(cola1.quitarcarlitos()))
                    input("Presione una tecla para continuar")
                else:
                    print("ERROR, el dato ingresado es un numero mayor al tamaño de la cola o no exite dicha cola.")
                    input("Presione una tecla para continuar")
            elif opc2 == "3":
                os.system("cls")
                print("*****Muestra los valores de la actual cola*****")
                cola1.mostrar()
                input("Presione una tecla para continuar")
            elif opc2 == "4":
                os.system("cls")
                print("*****Muestra la longitud de la Cola*****")
                print("La longitud de la cola es: {}, correcto?".format(cola1.longitud()))
                input("Presione una tecla para continuar")
            elif opc2 == "5":
                os.system("cls")
                print("*****Demuestra si la Cola está vacia*****")
                print("<False> en caso de que la cola está llena o tiene elementos y <True> para cuando la pila está vacia")
                print("{}".format(cola1.empty()))
                input("Presione una tecla para continuar")
            elif opc2 == "6":
                print("*****Regresará al Menu Principal*****")
                input("Presione una tecla para continuar")
            else:
                print("No valido")
                input("Presione una tecla para continuar")
                
                
                
                
                
                
                
                
    elif opc == "3":
        opc3 = ""
        while opc3 != "8":
            os.system("cls")
            men3 = Menu("****MENU LISTAS****", ["1)APPEND", "2)OBTENER", "3)OBTENER ELIMINADO", "4)BUSCAR", "5)INSERTAR", "6)ELIMINAR", "7)MOSTRAR", "8)SALIR"])
            opc3 = men3.menu()
            if opc3 == "1":
                os.system("cls")
                print("*****Se digitará  un número a la Lista*****")
                for i in range(tam):
                    dato = int(input("Inserte el numero que desea agregar a la lista: "))
                    lista1.append(dato)
                    print("Dato ingresado satisfactoriamente.")
                input("Presione una tecla para continuar")
            elif opc3 == "2":
                os.system("cls")
                print("*****Obtener un dato de una lista*****")
                pos =int(input("Inserte la posicion del dato: "))
                print(lista1.obtener(pos))
                input("Presione una tecla para continuar")
            elif opc3 == "3":
                os.system("cls")
                print("*****Obtener el valor eliminado junto a la lista*****")
                pos = int(input("Inserte la posicion del dato: "))
                lista1.obtenerEliminando(pos)
                input("Presione una tecla para continuar")
            elif opc3== "4":
                os.system("cls")
                print("*****Busca el elemento dentro de la lista y retorna la posicion*****")
                pos = int(input("Inserte el dato que desee buscar: "))
                print(lista1.buscar(pos))
                input("Presione una tecla para continuar")
            elif opc3 == "5":
                os.system("cls")
                print("*****Insertar dato en la lista sino existía ya en la lista*****")
                dato = int(input("Inserte el dato que quiera buscar para insertar: "))
                print(lista1.insertar(dato))
                input("Presione una tecla continuar")
            elif opc3 == "6":
                os.system("cls")
                print("*****Se elimina dato de la lista si existe en la lista*****")
                dato = int(input("Inserte el dato que quiera buscar para eliminarlo: "))
                print(lista1.eliminar(dato))
                input("Presione una tecla para continar")
            elif opc3 == "7":
                os.system("cls")
                print("*****Digite los datos de la lista*****")
                lista1.mostrar()
                input("Digite una tecla para continuar.")
            elif opc3 == "8":
                print("Regresara al Menu Principal")
                input("Presione una tecla  para continuar")
            else:
                print("no valida")
                input("Presione una tecla para continuar")
                
                
                
                
    elif opc == "4":
        print("See you later. :)")
    else:
        print("Opción no valida")
        input("Presione una tecla para continuar ")