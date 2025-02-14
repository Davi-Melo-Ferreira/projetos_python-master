class Media:
    def __init__(self, a, b, c, d):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)
        self.set_d(d)

    @property
    def values(self):
        return self._a
    
    def set_a(self, a):
        self._a = a
    
    def get_b(self):
        return self._b
    
    def set_b(self, b):
        self._b = b
    
    def get_c(self):
        return self._c
    
    def set_c(self, c):
        self._c = c
    
    def get_d(self):
        return self._d
    
    def set_d(self, d):
        self._d = d
    
    def calcular_media(self):
        self._media = (self._a + self._b + self._c + self._d) / 4
    
    def get_media(self):
        self.calcular_media()
        return self._media

valor = Media(2, 2, 2, 2)

print(f'{valor.get_media()}')