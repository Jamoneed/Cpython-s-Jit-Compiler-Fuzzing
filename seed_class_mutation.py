import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
from sys import stderr

class Counter:
    count = 0
    def increment(self):
        Counter.count += 1
        return Counter.count
    def get(self):
        return Counter.count

obj = Counter()

def uop_harness_f1(i):
    obj.increment()
    _ = obj.get()
    if i == 150:
        # This invalidates the JIT's inline cache for this class
        Counter.increment = lambda self: Counter.count + 100

for i in range(300):
    try:
        uop_harness_f1(i)
    except Exception as e:
        print(f"EXCEPTION: {e.__class__.__name__}: {e}", file=stderr)
        break
