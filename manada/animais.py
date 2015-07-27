class Animal():
    def __init__(self, nome, som):
        self._nome = nome
        self._som = som
    
    def barulho(self):
        raise NotImplementedError()

class Bicho(Animal):
    def barulho(self):
        return self._som

#class Gato(Animal):
#    def barulho(self):
#        return self._som