class ListaCarlitos:
    def __init__(self,tam=3):
        self.lista=[]
        self.longitud = 0
        self.size = tam

    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud += 1
            return True
        else:
            return False

    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            x = "el valor en la posicion {} es {}".format(pos,self.lista[pos])
            return x

    def obtenerEliminando(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            eliminado = self.lista[pos]
            self.lista = self.lista[:pos] + self.lista[pos+1:]
            print( "La lista queda tal que: {} y el elemento eliminado es {}".format(self.lista,eliminado))



    def buscar(self,dato):
        if dato in self.lista:
            self.res = self.lista.index(dato)
            print("la posicion del dato es ",self.res)
            return True
        else:
            return False


    def insertar(self,dato):
        if self.buscar(dato) == False:
            self.size += 1
            self.append(dato)
        return self.lista


    def eliminar(self,dato):
        if self.buscar(dato) == True:
            self.obtenerEliminando(self.res)
        else:
            False

    def mostrar(self):
        print("{:3}{:9}{}".format("","lista","posicion"))
        for pos, ele in enumerate(self.lista):
            print("[{:10}] {:3}".format(ele,pos))
