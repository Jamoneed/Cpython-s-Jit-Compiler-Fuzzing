import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
from sys import stderr

int_v1 = 99999
float_v1 = 3.14159
str_v1 = "test"

def add(a, b):
    return a + b

def uop_harness_f1(i):
    if i < 100:
        return add(int_v1, i)
    elif i < 200:
        return add(float_v1, float_v1)
    else:
        return add(str_v1, str_v1)

for i in range(300):
    try:
        uop_harness_f1(i)
    except Exception as e:
        print(f"EXCEPTION: {e.__class__.__name__}: {e}", file=stderr)
        break
