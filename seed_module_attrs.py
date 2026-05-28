import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
from sys import stderr
import math
import os

def uop_harness_f1():
    _ = math.pi
    _ = math.e
    _ = math.sqrt(4.0)
    _ = os.sep
    _ = os.path.join("a", "b")

for i in range(300):
    try:
        uop_harness_f1()
    except Exception as e:
        print(f"EXCEPTION: {e.__class__.__name__}: {e}", file=stderr)
        break
