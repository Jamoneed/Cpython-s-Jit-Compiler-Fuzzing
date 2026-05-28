import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
from sys import stderr

def uop_harness_f1():
    a1 = 1; a2 = 2; a3 = 3; a4 = 4; a5 = 5
    b1 = 1.1; b2 = 2.2; b3 = 3.3; b4 = 4.4; b5 = 5.5
    c1 = "a"; c2 = "b"; c3 = "c"; c4 = "d"; c5 = "e"
    d1 = [a1, b1]; d2 = [a2, b2]; d3 = [a3, b3]
    e1 = (a1, c1); e2 = (a2, c2); e3 = (a3, c3)
    total = a1 + a2 + a3 + a4 + a5
    total += b1 + b2 + b3 + b4 + b5
    for x in d1 + d2 + d3:
        total += x
    return total

for i in range(300):
    try:
        uop_harness_f1()
    except Exception as e:
        print(f"EXCEPTION: {e.__class__.__name__}: {e}", file=stderr)
        break
