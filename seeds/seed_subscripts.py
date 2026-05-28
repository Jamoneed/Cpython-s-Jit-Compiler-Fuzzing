import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
from sys import stderr

str_v1 = "hello world fuzzing"
tuple_v1 = (100, 200, 300, 400, 500)
list_v1 = [1, 2, 3, 4, 5, 6, 7, 8]

def uop_harness_f1(i):
    idx = i % 5
    _ = str_v1[idx]
    _ = tuple_v1[idx]
    _ = list_v1[idx]
    _ = str_v1[idx:idx+3]
    _ = list_v1[idx:idx+2]

for i in range(300):
    try:
        uop_harness_f1(i)
    except Exception as e:
        print(f"EXCEPTION: {e.__class__.__name__}: {e}", file=stderr)
        break
