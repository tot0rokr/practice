class A:
    def __init__(self, a):
        self._a = a
        self._b: int

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b


a = A(1)

print(a.a)

print(a.b)
