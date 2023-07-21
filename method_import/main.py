from functools import partial
import method_module

class Cls():
    def __init__(self, x):
        self.i = x
    def add_func(self, module):
        for m in dir(module):
            if not m.startswith('_'):
                setattr(self, m, partial(getattr(module, m), self))
