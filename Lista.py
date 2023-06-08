from  abc import ABC, abstractmethod

class ILista(ABC):
    @abstractmethod
    def insertarElemento (self, elemento, posicion):
        pass

    @abstractmethod
    def agregarElemento (self, elemento):
        pass

    @abstractmethod
    def mostrarElemento (self, posicion):
        pass

class Lista (ILista):
    __lista: list
    def __init__(self):
        self.__lista = []

    def insertarElemento(self, elemento, posicion):
        if posicion < 0 and posicion > len (self.__lista):
            raise Exception ('Error, posicion incorrecta')
        self.__lista.insert (posicion, elemento)

    def agregarElemento(self, elemento):
        self.__lista.append(elemento)

    def mostrarElemento(self, posicion):
        if posicion < 0 and posicion > len (self.__lista):
            raise Exception ('Error, posicion incorrecta')
        print (self.__lista[posicion])