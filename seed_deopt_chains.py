import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
def uop_harness_f1(i):
    a = 100; b = 200
    if i == 100: a = 3.14
    if i == 200: a = "str"
    try: return a + b
    except TypeError: return -1
for i in range(300):
    try: uop_harness_f1(i)
    except Exception: pass
