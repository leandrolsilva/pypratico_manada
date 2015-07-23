class Animal():
    def __init__(self, som = None):
        self._som = som
    
    def barulho(self):
        raise NotImplementedError()

class Cachorro(Animal):
    def __init__(self, som):
        super().__init__(som)
        
    def barulho(self):
        return self._som
