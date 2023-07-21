import sys

class Abs:
    def __iter__(self):
        for key in self.__dict__:
            yield key, getattr(self, key)
class A(Abs):
    def __init__(self):
        self.a = 1
        self.b = B()

class B(Abs):
    def __init__(self):
        self.a = 2.2
        self.b = [C() for _ in range(5)]

    def __str__(self):
        return str({k: str(v) for k, v in vars(self).items()})

class C(Abs):
    def __init__(self):
        self.a = hex(3)
    def __str__(self):
        return str({k: str(v) for k, v in vars(self).items()})


print(sys.argv)
