"""
Minimized reproducer for gh-144681
JIT assertion failure: Python/optimizer.c:790
jump_happened == (target_instr[1].cache & 1)

Crashing build:  CPython 3.15.0a6+ (heads/main-dirty:6908372fb81, March 2 2026)
Fixed build:     CPython 3.15.0a7+ (c32e264227b)
Crash command:   PYTHON_JIT=1 ~/fuzzing/cpython/python gh144681_crash.py
Clean command:   PYTHON_JIT=0 ~/fuzzing/cpython/python gh144681_crash.py
Fix:             PR #144742 — Fix JIT trace builder assertion failure when
                 conditional branch jump target coincides with fallthrough target

Root cause:
The JIT optimizer maintains an internal flag 'jump_happened' while building
a trace. The Tier 1 interpreter maintains a cache alongside each instruction
where the lowest bit of target_instr[1].cache reflects jump information.
When func.__code__ is replaced at runtime, the JIT traces the replacement
bytecode but reads stale cache entries from the original. The two disagree
and the assertion fires.
"""

def original():
    return 1

def replacement():
    return 'a_string'

# Warm up the JIT with the original function
for i in range(102):
    try:
        original()
    except Exception:
        pass

# Replace the code object while the JIT has cached the original's structure
original.__code__ = replacement.__code__

# JIT traces replacement bytecode with original's stale inline cache entries
# This triggers the assertion failure on affected builds
for _ in range(100):
    try:
        original()
    except Exception:
        pass
