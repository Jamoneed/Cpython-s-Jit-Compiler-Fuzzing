import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
import gc
class CyclicNode:
    def __init__(self, val): self.val = val; self.ref = None
def uop_harness_f1(i):
    a = CyclicNode(i); b = CyclicNode(i + 1)
    a.ref = b; b.ref = a
    result = a.val + b.val
    if i % 50 == 0: gc.collect()
    return result
for i in range(300):
    try: uop_harness_f1(i)
    except Exception: pass
