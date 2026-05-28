import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
from sys import stderr

int_v1 = 42
int_v2 = 0
str_v1 = "nonempty"
str_v2 = ""
list_v1 = [1, 2, 3]
none_v = None

def uop_harness_f1():
    _ = not int_v1
    _ = not int_v2
    _ = int_v1 if str_v1 else int_v2
    _ = none_v is None
    _ = int_v1 is not None
    if list_v1:
        pass
    while int_v2 < 3:
        int_v2 += 1
    int_v2 = 0

for i in range(300):
    try:
        uop_harness_f1()
    except Exception as e:
        print(f"EXCEPTION: {e.__class__.__name__}: {e}", file=stderr)
        break
