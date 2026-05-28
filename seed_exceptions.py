import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
from sys import stderr

def risky(x):
    if x % 7 == 0:
        raise ValueError(f"bad value: {x}")
    return x * 2

def uop_harness_f1(i):
    try:
        result = risky(i)
    except ValueError:
        result = -1
    return result

for i in range(300):
    try:
        uop_harness_f1(i)
    except Exception as e:
        print(f"EXCEPTION: {e.__class__.__name__}: {e}", file=stderr)
        break
