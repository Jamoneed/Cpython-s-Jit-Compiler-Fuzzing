import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
def uop_harness_f1(i):
    x = i % 7
    if x == 0: return [j * 2 for j in range(10)]
    elif x == 1: return {j: j**2 for j in range(10)}
    elif x == 2: return tuple(range(10))
    elif x == 3: return sum(range(100))
    elif x == 4: return "".join(str(j) for j in range(10))
    elif x == 5: return frozenset(range(10))
    else: return bytearray(b"fuzzing")
for i in range(300):
    try: uop_harness_f1(i)
    except Exception: pass
