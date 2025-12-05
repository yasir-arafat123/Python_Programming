# Time Module

## Overview

The `time` module provides functions for working with time values, measuring execution time, pausing programs, and handling timestamps. It's distinct from `datetime` - while datetime handles calendar dates and human-readable times, `time` focuses on system-level timing operations.

## Core Things to Learn

### 1. Time Measurement Functions

**Current Time**
```python
import time

# Seconds since Unix epoch (Jan 1, 1970, 00:00:00 UTC)
timestamp = time.time()  # e.g., 1701388234.567

# High-resolution timer for performance measurement
start = time.perf_counter()
# ... code to measure ...
elapsed = time.perf_counter() - start

# Monotonic clock (never goes backwards, immune to system clock adjustments)
start = time.monotonic()
# ... code to measure ...
elapsed = time.monotonic() - start

# CPU time (time spent in current process)
cpu_time = time.process_time()
```

### 2. Pausing Execution

```python
import time

# Sleep for specified seconds (accepts float for milliseconds)
time.sleep(1)        # 1 second
time.sleep(0.5)      # 500 milliseconds
time.sleep(0.001)    # 1 millisecond
```

### 3. Time Conversion

```python
import time

# Convert timestamp to struct_time (local time)
timestamp = time.time()
local_time = time.localtime(timestamp)
print(local_time.tm_year, local_time.tm_mon, local_time.tm_mday)

# Convert timestamp to struct_time (UTC)
utc_time = time.gmtime(timestamp)

# Convert struct_time to string
time_str = time.strftime('%Y-%m-%d %H:%M:%S', local_time)

# Convert struct_time to timestamp
timestamp = time.mktime(local_time)
```

### 4. Timing Context Managers

**Modern approach** (Python 3.7+):
```python
import time
from contextlib import contextmanager

@contextmanager
def timer(label="Operation"):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label}: {elapsed:.4f}s")

with timer("Database query"):
    # ... database operation ...
    time.sleep(0.5)
```

## When to Use time vs datetime

| Use `time` | Use `datetime` |
|------------|----------------|
| Benchmarking code performance | Working with dates and calendars |
| Measuring elapsed time | Parsing/formatting human-readable times |
| Pausing execution | Time zone conversions |
| Low-level system timestamps | Date arithmetic (add days, months) |
| Rate limiting | Scheduling (cron-like tasks) |

## Common Use Cases

1. **Performance measurement** (profiling, benchmarking)
2. **Rate limiting** (API throttling, request spacing)
3. **Polling loops** (check status every N seconds)
4. **Timeouts** (operation must complete in X seconds)
5. **Delays** (retry after cooldown, animation timing)
6. **Timestamping** (logging, cache invalidation)

## Python Libraries

| Function | Purpose | Best For |
|----------|---------|----------|
| `time.time()` | Wall-clock time | Timestamps, logging |
| `time.perf_counter()` | High-resolution timer | **Benchmarking** (recommended) |
| `time.monotonic()` | Monotonic clock | **Timeouts, intervals** |
| `time.process_time()` | CPU time | CPU profiling |
| `time.sleep()` | Pause execution | Delays, polling |

**Why perf_counter() for benchmarking?**
- Highest available resolution
- Includes time during sleep
- Best for measuring short durations

**Why monotonic() for timeouts?**
- Never decreases (immune to system clock changes)
- Reliable for measuring intervals
- Won't break if user adjusts system time

## Best Practices

### 1. Always Use perf_counter() for Benchmarking
```python
# ❌ BAD: time() has lower resolution
start = time.time()
result = compute()
print(time.time() - start)

# ✅ GOOD: perf_counter() is precise
start = time.perf_counter()
result = compute()
print(time.perf_counter() - start)
```

### 2. Use monotonic() for Timeouts
```python
# ❌ BAD: time() can go backwards (daylight saving, NTP sync)
deadline = time.time() + timeout
while time.time() < deadline:
    if check_condition():
        break

# ✅ GOOD: monotonic() is reliable
deadline = time.monotonic() + timeout
while time.monotonic() < deadline:
    if check_condition():
        break
```

### 3. Sleep in Loops Responsibly
```python
# ❌ BAD: tight loop wastes CPU
while not condition:
    pass  # 100% CPU usage

# ✅ GOOD: sleep between checks
while not condition:
    time.sleep(0.1)  # Check every 100ms, gentle on CPU
```

### 4. Handle Sleep Interruptions
```python
import time
import signal

# sleep() can be interrupted by signals on Unix
try:
    time.sleep(10)
except KeyboardInterrupt:
    print("Sleep interrupted by Ctrl+C")
```

## Common Patterns

### Rate Limiting
```python
import time

def rate_limited_api_call(calls_per_second=5):
    min_interval = 1.0 / calls_per_second
    last_call = 0
    
    def call():
        nonlocal last_call
        elapsed = time.perf_counter() - last_call
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)
        last_call = time.perf_counter()
        # ... make API call ...
    
    return call
```

### Retry with Exponential Backoff
```python
import time

def retry_with_backoff(func, max_retries=3, base_delay=1):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)
```

### Timeout Decorator
```python
import time
import signal

def timeout(seconds):
    def decorator(func):
        def handler(signum, frame):
            raise TimeoutError(f"Function timed out after {seconds}s")
        
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)
        return wrapper
    return decorator
```

## Performance Considerations

```python
# Resolution comparison
print(f"time() resolution: ~{time.get_clock_info('time').resolution}s")
print(f"perf_counter() resolution: ~{time.get_clock_info('perf_counter').resolution}s")

# Typical output:
# time() resolution: ~0.001s (1ms)
# perf_counter() resolution: ~0.000001s (1µs)
```

## Visualize It

- [Time module tutorial](https://realpython.com/python-time-module/)
- [Understanding Python timing](https://www.webucator.com/article/python-clocks-explained/)

## References

- [Python time docs](https://docs.python.org/3/library/time.html)
- [PEP 418 - Monotonic Time](https://peps.python.org/pep-0418/)
- [timeit for microbenchmarking](https://docs.python.org/3/library/timeit.html)
- Python roadmap — https://roadmap.sh/python

## Related Topics

- `I.8/4_Dates_datetime` - Calendar dates and times
- `P.15_Performance/01_timeit` - Accurate microbenchmarking
- `O.14_Concurrency/01_Threading` - Thread sleep and synchronization
- `M.12_Errors_Robust` - Timeout patterns and retry logic
- `Real_World_Applications/08_Performance_Engineering` - Performance profiling
