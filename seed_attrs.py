import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
from sys import stderr

int_v1 = 12345
str_v1 = "hello world"
float_v1 = 3.14

class MyClass:
    x = 100
    def method(self):
        return self.x * 2

obj = MyClass()

def uop_harness_f1():
    _ = obj.x
    _ = obj.method()
    _ = str_v1.upper()
    _ = str_v1.split()

for i in range(300):
    try:
        uop_harness_f1()
    except Exception as e:
        print(f"EXCEPTION: {e.__class__.__name__}: {e}", file=stderr)
        break
