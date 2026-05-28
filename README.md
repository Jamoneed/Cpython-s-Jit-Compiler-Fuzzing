# CPython JIT Compiler Fuzzing

Coverage-guided fuzzing campaign and low-memory stress testing framework targeting CPython's experimental Tier 2 JIT compiler. Masters thesis research, UCI 2026.

## Overview

This repository archives the research artifacts from two complementary research tracks against CPython's experimental JIT compiler (`--enable-experimental-jit`), conducted as part of a Masters thesis at UC Irvine.

## Track 1 — Coverage-guided fuzzing with lafleur

Uses lafleur, a UOP edge coverage-guided evolutionary fuzzer, to target CPython 3.15's Tier 2 JIT compiler across six parallel build configurations: debug, differential, free-threaded, AddressSanitizer, UndefinedBehaviorSanitizer, and a RAM-disk instance. The campaign independently rediscovered gh-144681, a confirmed JIT assertion failure in `Python/optimizer.c` triggered by runtime code object mutation (`func.__code__ = other.__code__`), validating that the setup correctly targets real JIT vulnerabilities.

## Track 2 — Low-memory stress testing

An 11-phase framework testing JIT behavior under memory pressure using ulimit virtual memory caps, LD_PRELOAD fault injection targeting JIT executable page allocations, deterministic per-allocation failure walking via a direct patch to `jit_alloc` in `Python/jit.c`, concurrent thread stress testing, ASAN under pressure, trace cache exhaustion, trace invalidation racing, real-world package testing via labeille, lafleur mutations under memory pressure, libfiu precise fault injection, and performance characterization. Developed in collaboration with a CPython JIT maintainer.

## Contents

- `seeds/` — 18 hand-rolled seed files targeting specific JIT UOP families
- `lowmem/` — complete low-memory stress testing framework including fail_mmap.c, fail_malloc.c, harness.py, and all phase runner scripts
- `reproducers/` — minimized reproducer for gh-144681
- `scripts/` — campaign launch configuration for six parallel lafleur instances

## Related

- [lafleur](https://github.com/devdanzin/lafleur) — the fuzzer used in this campaign
- [gh-144681](https://github.com/python/cpython/issues/144681) — the bug independently rediscovered
- [PR #144742](https://github.com/python/cpython/pull/144742) — the fix
