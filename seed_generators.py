import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
from sys import stderr

list_v1 = [1, 2, 3, 4, 5]
tuple_v1 = (10, 20, 30)

def gen_squares(n):
    for i in range(n):
        yield i * i

def uop_harness_f1():
    total = 0
    for x in list_v1:
        total += x
    for x in tuple_v1:
        total += x
    for x in range(10):
        total += x
    g = gen_squares(5)
    result = list(g)
    return total, result

for i in range(300):
    try:
        uop_harness_f1()
    except Exception as e:
        print(f"EXCEPTION: {e.__class__.__name__}: {e}", file=stderr)
        break
