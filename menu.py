import os
from Listas import Lista
from Pila import Pila
from Cola import Cola

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
                opc = input("Eliga una opcion [1....{}]: ".format(len(self.opciones)))
                break
            except ValueError:
                print("Dato no válido, trata de ingresar un número")
        return opc
opc = ""
while True:
    try:
        tam = int(input("Ingrese tamaño de la lista/pila/cola: "))
        break
    except ValueError:
        print("Dato no válido, Trata de ingresar un número")
pila1 = Pila(tam)
lista1 = Lista(tam)
cola1 = Cola(tam)
while opc != "4":
    os.system("cls")
    men = Menu("---Menú Principal---",
               ["1)Pila", "2)Cola", "3)Lista", "4)Salir"])
    opc = men.menu()
    if opc == "1":
        opc1 =""
        while opc1 != "6":
            os.system("cls")
            men1 = Menu("---Menu Pila---",["1)Push","2)Pop","3)Show","4)Longitud","5)Empty","6)Salir"])
            opc1 = men1.menu()
            if opc1 =="1":
                os.system("cls")
                print("Digite un numero a la Pila")
                for i in range(tam):
                    while True:
                        try:
                            dato = int(input("Digite el numero que desea dar a la pila: "))
                            break
                        except ValueError:
                            print("Dato no válido, Trate de ingresar un número")
                    pila1.push(dato)
                    print("Dato ingresado")
                input("Da click para continuar")
            elif opc1 == "2":
                os.system("cls")
                print("Retira el ultimo digito de la Pila")
                while True:
                    try:
                        x = int(input("Cuantos elemento desea quitar de la Pila: "))
                        break
                    except ValueError:
                        print("Dato no válido, Trate de ingresar un número")
                if x <= tam:
                    for i in range(x):
                        print("El elemento quitado es: {}".format(pila1.pop()))
                    input("Da click para continuar")
                else:
                    print("ERROR numero mayor al tamaño de la pila o no exite una pila")
                    input("Da click para continuar")
            elif opc1 =="3":
                os.system("cls")
                print("Muestre los valores de la Pila")
                pila1.show()
                input("Da click para continuar")
            elif opc1 == "4":
                os.system("cls")
                print("Muestre la longitud de la Pila")
                print("Longitud de la pila es: {}".format(pila1.longitud()))
                input("Da click para continuar")
            elif opc1 =="5":
                os.system("cls")
                print("Demuestre si la Pila esta vacia")
                print("False para pila llena y True para pila vacia")
                print("---{}---".format(pila1.empty()))
                input("Da click para continuar")
            elif opc1 =="6":
                print("Vuelva al Menu Principal")
                input("Da click para continuar")
            else:
                print("no valida")
                input("Da click para continuar")
    elif opc == "2":
        opc2 = ""
        while opc2 != "6":
            os.system("cls")
            men2 = Menu("Menu Cola", ["1)Insertar", "2)Quitar", "3)Mostrar", "4)Longitud", "5)Empty", "6)Salir"])
            opc2 = men2.menu()
            if opc2 == "1":
                os.system("cls")
                print("Ingreso de un numero a la Cola")
                for i in range(tam):
                    dato = int(input("Digite el numero que desea poner a la cola: "))
                    cola1.insentar(dato)
                    print("Dato ingresado")
                input("Da click para continuar")
            elif opc2 == "2":
                os.system("cls")
                print("Sacar el primer valor de la cola")
                x = int(input("Cuantos elemento se van a quitar de la cola: "))
                if x <= tam:
                    for i in range(x):
                        print("El elemento quitado es: {}".format(cola1.quitar()))
                    input("Da click para continuar")
                else:
                    print("ERROR numero mayor al tamaño de la cola o no exite una cola")
                    input("Da click para continuar")
            elif opc2 == "3":
                os.system("cls")
                print("Muestre los valores de la cola")
                cola1.mostrar()
                input("Da click para continuar")
            elif opc2 == "4":
                os.system("cls")
                print("Muestre la longitud de la Cola")
                print("La longitud de la cola es: {}".format(cola1.longitud()))
                input("Da click para continuar")
            elif opc2 == "5":
                os.system("cls")
                print("Demuestre si la Cola está vacia---")
                print("False para cola llena o tiene elementos y True para pila vacia")
                print("{}".format(cola1.empty()))
                input("Da clicl para continuar")
            elif opc2 == "6":
                print("Regrese al Menu Principal")
                input("Da clicl para continuar")
            else:
                print("no valida")
                input("Da click para continuar")
    elif opc == "3":
        opc3 = ""
        while opc3 != "8":
            os.system("cls")
            men3 = Menu("Menu Listas", ["1)Append", "2)Obtener", "3)ObtenerEliminado", "4)Buscar", "5)Insertar", "6)Eliminar", "7)Mostrar", "8)Salir"])
            opc3 = men3.menu()
            if opc3 == "1":
                os.system("cls")
                print("Se digitara  un numero a la Lista---")
                for i in range(tam):
                    dato = int(input("Digite el numero que desea ingresar a la lista: "))
                    lista1.append(dato)
                    print("Dato ingresado")
                input("Da click para continuar")
            elif opc3 == "2":
                os.system("cls")
                print("Tener un dato de una lista")
                pos =int(input("Digite posicion del dato: "))
                print(lista1.obtener(pos))
                input("Da click  para continuar")
            elif opc3 == "3":
                os.system("cls")
                print("Tener el valor eliminado junto a la lista")
                pos = int(input("Digite la posicion del dato: "))
                lista1.obtenerEliminando(pos)
                input("Da click para continuar")
            elif opc3== "4":
                os.system("cls")
                print("Busca el elemento en la lista y retornar la posicion")
                pos = int(input("Ingresa el dato a buscar: "))
                print(lista1.buscar(pos))
                input("Da click para continuar")
            elif opc3 == "5":
                os.system("cls")
                print("Insertar dato en la lista sino existía ya en la lista")
                dato = int(input("Digite el dato a buscar para insertarlo: "))
                print(lista1.insertar(dato))
                input("Da click para  continuar")
            elif opc3 == "6":
                os.system("cls")
                print("Se elimina dato de la lista si existe en la lista")
                dato = int(input("Ingres dato a buscar para eliminarlo: "))
                print(lista1.eliminar(dato))
                input("Da click para continar")
            elif opc3 == "7":
                os.system("cls")
                print("Digite los datos de la lista")
                lista1.mostrar()
                input("Digite una tecla para continuar")
            elif opc3 == "8":
                print("Regrese al Menu Principal")
                input("Da click  para continuar")
            else:
                print("no valida")
                input("Da click para continuar")
    elif opc == "4":
        print("Te esperamos pronto")
    else:
        print("Opción no valida")
        input("Da click para continuar ")