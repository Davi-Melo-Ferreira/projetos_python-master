class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, a):
        self._a = a
    
    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, b):
        self._b = b
    
    def somar(self):
        pass

class B(A):
    def __init__(self, a, b):
        super().__init__(a, b)
    
    def somar(self):
        pass

class C(B, A):
    def __init__(self, a, b):
        super().__init__(a, b)
