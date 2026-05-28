import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
from sys import stderr

int_v1 = 600627076259156299
int_v2 = 52508104421
float_v1 = -5.1
float_v2 = 997.726

def uop_harness_f1():
    _ = int_v1 + int_v2
    _ = int_v1 - int_v2
    _ = int_v1 * int_v2
    _ = float_v1 * float_v2
    _ = float_v1 + float_v2
    _ = int_v1 > int_v2
    _ = float_v1 < float_v2
    _ = int_v1 == int_v2

for i in range(300):
    try:
        uop_harness_f1()
    except Exception as e:
        print(f"EXCEPTION: {e.__class__.__name__}: {e}", file=stderr)
        break
