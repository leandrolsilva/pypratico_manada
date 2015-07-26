class Manada(object):
    def __init__(self):
        self._animais = {}
    
    def adicionar_animal(self, cls_animal):
        self._animais[cls_animal._nome] = cls_animal
    
    def animal(self, animal):
        return self._animais[animal]
    
    def barulho(self, separador = "\n"):
        sons = []
        for animal, cls_animal in self._animais.items():
            sons.append(cls_animal._som)
        return separador.join(sons)

if __name__ == '__main__':
    import animais
    c = animais.Bicho('Cachorro', 'Au')
    g = animais.Bicho('Gato', 'Miau')
    b = animais.Bicho('Boi', 'Muuuu')
    
    m = Manada()
    m.adicionar_animal(c)
    m.adicionar_animal(g)
    m.adicionar_animal(b)
    print(m.barulho())
    print(m.barulho(','))
    print(m.barulho('-'))