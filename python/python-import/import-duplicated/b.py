print("b.py")

__global = None
if not __global:
    print("b.global")
    __global = 1

class A:
    def __init__(self):
        print("b.A")

class B:
    def __init__(self):
        print("b.B")
