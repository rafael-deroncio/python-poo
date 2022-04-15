class ControleRemoto():

    def __init__(self):
        self.__ligado = False
    
    @property
    def ligado(self):
        return self.__ligado
    
    @ligado.setter
    def ligado(self, ligar):
        self.ligado = ligar

c1 = ControleRemoto

print(c1.ligado)

c1.ligado = True

print(c1.ligado)
