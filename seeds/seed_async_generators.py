import sys
print("[f1] STRATEGY: fuzzing", file=sys.stderr)
import asyncio
async def async_gen(n):
    for i in range(n): yield i * 2
async def consumer():
    result = 0
    async for val in async_gen(10): result += val
    return result
def uop_harness_f1(i): return asyncio.run(consumer())
for i in range(300):
    try: uop_harness_f1(i)
    except Exception: pass
