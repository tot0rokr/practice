import pathlib

print(__file__)
print(pathlib.Path(__file__).parent / "zxc.txt")
print(pathlib.Path("zxc.txt"))
print(pathlib.Path("zxc.txt").parent)
