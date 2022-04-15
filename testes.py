from abc import ABC, abstractmethod

class Controlador(ABC):
    
    def ligar():
        pass

    def desligar():
        pass

    def abrirMenu():
        pass

    def fecharMenu():
        pass

    def maisVolume():
        pass

    def menosVolume():
        pass

    def ligaMudo():
        pass

    def desligaMudo():
        pass

    def play():
        pass

    def pause():
        pass

class ControleRemoto(Controlador):
    
    def __init__(self):
        self.__ligado = False
        self.__tocando = False
        self.__mudo = False
        self.__volume = 50
            
    @property
    def ligado(self):
        return self.__ligado
    
    @ligado.setter
    def ligado(self, ligado):
        self.ligado = ligado

    @property
    def tocando(self):
        return self.__tocando
    
    @tocando.setter
    def tocando(self, tocando):
        self.tocando = tocando

    @property
    def mudo(self):
        return self.__mudo
    
    @mudo.setter
    def mudo(self, mudo):
        self.mudo = mudo

    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, volume):
        self.volume = volume

    @classmethod
    def ligar(self):
        if not self.ligado:
            self.ligado = True
        print(f'Ligado: {self.ligado}')

    @classmethod
    def desligar(self):
        if self.ligado:
            self.ligado = False
        print(f'Ligado: {self.ligado}')

    def abrirMenu():
        pass

    def fecharMenu():
        pass

    def maisVolume():
        pass

    def menosVolume():
        pass

    def ligaMudo():
        pass

    def desligaMudo():
        pass

    def play():
        pass

    def pause():
        pass

controle = ControleRemoto

controle.ligar()