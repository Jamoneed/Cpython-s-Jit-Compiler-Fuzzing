import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
from sys import stderr

def make_counter(start=0):
    count = start
    def increment(by=1):
        nonlocal count
        count += by
        return count
    def reset():
        nonlocal count
        count = 0
    return increment, reset

inc, rst = make_counter()

def uop_harness_f1():
    inc()
    inc(by=2)
    inc(by=3)

for i in range(300):
    try:
        uop_harness_f1()
        if i % 50 == 0:
            rst()
    except Exception as e:
        print(f"EXCEPTION: {e.__class__.__name__}: {e}", file=stderr)
        break
