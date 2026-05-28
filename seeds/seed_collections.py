import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
from sys import stderr

int_v1 = 42
float_v1 = 3.14
str_v1 = "hello"
bool_v1 = True

def uop_harness_f1():
    lst = [int_v1, float_v1, str_v1, bool_v1]
    tup = (int_v1, float_v1)
    st  = {int_v1, int_v1 + 1, int_v1 + 2}
    dct = {"a": int_v1, "b": float_v1}
    fst = f"{str_v1} = {int_v1}"
    lst.append(fst)
    _ = dct["a"]
    _ = int_v1 in st

for i in range(300):
    try:
        uop_harness_f1()
    except Exception as e:
        print(f"EXCEPTION: {e.__class__.__name__}: {e}", file=stderr)
        break
