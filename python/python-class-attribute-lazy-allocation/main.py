class BaseClass:
    handler: None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.handler = None
        for _, method in cls.__dict__.copy().items():
            if hasattr(method, '_is_handler'):
                cls.handler = method
                delattr(method, '_is_handler')

    @staticmethod
    def handler_decorator(func):
        def wrapper(self, *args, **kwargs):
            return func(self, *args, **kwargs)
        setattr(wrapper, '_is_handler', True)
        return wrapper

    def call_handler(self):
        self.handler()

class ConcreteClass1(BaseClass):
    @BaseClass.handler_decorator
    def method1(self):
        print("Method 1")

class ConcreteClass2(BaseClass):
    @BaseClass.handler_decorator
    def method2(self):
        print("Method 2")

if __name__ == '__main__':
    print(ConcreteClass1.handler)
    print(ConcreteClass2.handler)

    ConcreteClass1().call_handler()
    ConcreteClass2().call_handler()
