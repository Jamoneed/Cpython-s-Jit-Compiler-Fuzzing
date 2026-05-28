#!/bin/bash
# lafleur Campaign Launch Script
# Launches 6 parallel fuzzing instances in a tmux session
# Target: CPython 3.15.0a7+ with --with-pydebug --enable-experimental-jit

CAMPAIGN_DIR=~/fuzzing/campaign1
CORPUS_DIR=$CAMPAIGN_DIR/corpus/jit_interesting_tests
PYTHON_DEBUG=~/fuzzing/cpython/python
PYTHON_FT=~/fuzzing/cpython_freethreaded/python
PYTHON_ASAN=~/fuzzing/cpython_asan/python
PYTHON_UBSAN=~/fuzzing/cpython_ubsan/python
RAM_DISK=/mnt/fuzz_ram
RAM_CAMPAIGN=$RAM_DISK/campaign_fast

source ~/fuzzing/lafleur_venv/bin/activate

# Set up RAM disk campaign directory
mkdir -p $RAM_CAMPAIGN/corpus/jit_interesting_tests
cp $CORPUS_DIR/*.py $RAM_CAMPAIGN/corpus/jit_interesting_tests/ 2>/dev/null || true

# Create tmux session
tmux new-session -d -s fuzz_campaign -n debug-1

# Window 1: debug-1 — debug+JIT, dynamic runs, deepening
tmux send-keys -t fuzz_campaign:debug-1 \
    "source ~/fuzzing/lafleur_venv/bin/activate && \
    cd $CAMPAIGN_DIR && \
    lafleur \
    --target-python $PYTHON_DEBUG \
    --min-corpus-files 20 \
    --dynamic-runs \
    --deepening-probability 0.3 \
    --runs 3 \
    --instance-name debug-1" C-m

# Window 2: diff-1 — differential testing for silent wrong-result bugs
tmux new-window -t fuzz_campaign -n diff-1
tmux send-keys -t fuzz_campaign:diff-1 \
    "source ~/fuzzing/lafleur_venv/bin/activate && \
    cd $CAMPAIGN_DIR && \
    lafleur \
    --target-python $PYTHON_DEBUG \
    --min-corpus-files 20 \
    --differential-testing \
    --instance-name diff-1" C-m

# Window 3: freethreaded-1 — free-threaded build for GIL-free race conditions
tmux new-window -t fuzz_campaign -n freethreaded-1
tmux send-keys -t fuzz_campaign:freethreaded-1 \
    "source ~/fuzzing/lafleur_venv/bin/activate && \
    cd $CAMPAIGN_DIR && \
    lafleur \
    --target-python $PYTHON_FT \
    --min-corpus-files 20 \
    --dynamic-runs \
    --deepening-probability 0.3 \
    --instance-name freethreaded-1" C-m

# Window 4: asan-1 — ASAN build for heap corruption and use-after-free
tmux new-window -t fuzz_campaign -n asan-1
tmux send-keys -t fuzz_campaign:asan-1 \
    "source ~/fuzzing/lafleur_venv/bin/activate && \
    cd $CAMPAIGN_DIR && \
    ASAN_OPTIONS='detect_leaks=0:abort_on_error=1' \
    lafleur \
    --target-python $PYTHON_ASAN \
    --min-corpus-files 20 \
    --dynamic-runs \
    --instance-name asan-1" C-m

# Window 5: ubsan-1 — UBSAN build for undefined behavior
tmux new-window -t fuzz_campaign -n ubsan-1
tmux send-keys -t fuzz_campaign:ubsan-1 \
    "source ~/fuzzing/lafleur_venv/bin/activate && \
    cd $CAMPAIGN_DIR && \
    lafleur \
    --target-python $PYTHON_UBSAN \
    --min-corpus-files 20 \
    --dynamic-runs \
    --instance-name ubsan-1" C-m

# Window 6: ram-fast-1 — debug+JIT on tmpfs RAM disk for breadth-first coverage
tmux new-window -t fuzz_campaign -n ram-fast-1
tmux send-keys -t fuzz_campaign:ram-fast-1 \
    "source ~/fuzzing/lafleur_venv/bin/activate && \
    cd $RAM_CAMPAIGN && \
    lafleur \
    --target-python $PYTHON_DEBUG \
    --min-corpus-files 20 \
    --deepening-probability 0.1 \
    --instance-name ram-fast-1" C-m

# Set up crash backup cron job (every 2 hours)
(crontab -l 2>/dev/null; echo "0 */2 * * * ~/fuzzing/backup_crashes.sh") | crontab -

echo "6 instances running — tmux attach -t fuzz_campaign"
echo "Ctrl+B n = next window | Ctrl+B p = prev | Ctrl+B d = detach"
