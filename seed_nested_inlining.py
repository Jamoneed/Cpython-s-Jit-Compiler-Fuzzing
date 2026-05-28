import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
def leaf(x): return x + 1
def mid(x): return leaf(x) * 2
def outer(x): return mid(x) + mid(x + 1)
def uop_harness_f1(i):
    a = outer(i); b = outer(a); c = leaf(b)
    if i == 150:
        global leaf
        leaf = lambda x: x - 1
    return c
for i in range(300):
    try: uop_harness_f1(i)
    except Exception: pass
