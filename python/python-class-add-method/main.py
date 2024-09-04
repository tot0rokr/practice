from functools import partial
import method_module

class Cls():
    def __init__(self, x):
        self.i = x
    def add_func(self):
        for m in dir(method_module):
            if not m.startswith('_'):
                setattr(self, m, partial(getattr(method_module, m), self))
