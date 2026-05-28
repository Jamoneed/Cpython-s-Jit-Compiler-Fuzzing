import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
class Stable:
    __slots__ = ('x',)
    def __init__(self): self.x = 42
class Mutable:
    def __init__(self): self.x = 42
def uop_harness_f1(i):
    if i < 150: obj = Stable()
    else:
        obj = Mutable()
        if i == 200:
            obj.__class__ = type('Hijacked', (), {'x': property(lambda s: 999)})
    return obj.x
for i in range(300):
    try: uop_harness_f1(i)
    except Exception: pass
