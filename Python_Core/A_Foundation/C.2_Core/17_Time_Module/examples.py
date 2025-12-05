"""Examples for Time Module."""

import time
import random
from contextlib import contextmanager


# ============================================================================
# Example 1: Basic Time Measurement
# ============================================================================

def basic_time_example():
    """Understand different time functions."""
    print("=== Basic Time Functions ===\n")
    
    # Current timestamp (seconds since epoch)
    timestamp = time.time()
    print(f"Current timestamp: {timestamp}")
    print(f"Readable: {time.ctime(timestamp)}")
    
    # High-resolution timer
    perf_start = time.perf_counter()
    time.sleep(0.1)
    perf_elapsed = time.perf_counter() - perf_start
    print(f"\nperf_counter elapsed: {perf_elapsed:.6f}s")
    
    # Monotonic clock
    mono_start = time.monotonic()
    time.sleep(0.1)
    mono_elapsed = time.monotonic() - mono_start
    print(f"monotonic elapsed: {mono_elapsed:.6f}s")
    
    # CPU time
    cpu_start = time.process_time()
    # CPU-intensive work
    total = sum(i**2 for i in range(100000))
    cpu_elapsed = time.process_time() - cpu_start
    print(f"\nCPU time for computation: {cpu_elapsed:.6f}s")


# ============================================================================
# Example 2: Benchmarking Code Performance
# ============================================================================

def benchmark_example():
    """Measure code execution time."""
    print("\n=== Benchmarking ===\n")
    
    def slow_function():
        """Simulate slow operation."""
        time.sleep(0.05)
        return sum(i for i in range(100000))
    
    def fast_function():
        """Simulate fast operation."""
        return sum(range(100000))
    
    # Benchmark slow function
    start = time.perf_counter()
    result1 = slow_function()
    slow_time = time.perf_counter() - start
    
    # Benchmark fast function
    start = time.perf_counter()
    result2 = fast_function()
    fast_time = time.perf_counter() - start
    
    print(f"Slow function: {slow_time:.6f}s")
    print(f"Fast function: {fast_time:.6f}s")
    print(f"Speedup: {slow_time/fast_time:.2f}x faster")


# ============================================================================
# Example 3: Sleep and Delays
# ============================================================================

def sleep_example():
    """Use sleep for delays and rate limiting."""
    print("\n=== Sleep Operations ===\n")
    
    # Basic sleep
    print("Sleeping for 1 second...")
    time.sleep(1)
    print("Done!")
    
    # Fractional sleep (milliseconds)
    print("\nSleeping for 500ms...")
    time.sleep(0.5)
    print("Done!")
    
    # Progress indicator
    print("\nProgress: ", end='', flush=True)
    for i in range(5):
        print(".", end='', flush=True)
        time.sleep(0.2)
    print(" Complete!")


# ============================================================================
# Example 4: Rate Limiting
# ============================================================================

def rate_limiting_example():
    """Implement rate limiting for API calls."""
    print("\n=== Rate Limiting ===\n")
    
    class RateLimiter:
        """Simple rate limiter."""
        def __init__(self, calls_per_second):
            self.min_interval = 1.0 / calls_per_second
            self.last_call = 0
        
        def wait(self):
            """Wait if necessary to maintain rate limit."""
            elapsed = time.perf_counter() - self.last_call
            if elapsed < self.min_interval:
                time.sleep(self.min_interval - elapsed)
            self.last_call = time.perf_counter()
    
    # Simulate API calls (5 calls per second)
    limiter = RateLimiter(calls_per_second=5)
    
    print("Making rate-limited API calls (5/sec):")
    start_time = time.perf_counter()
    
    for i in range(10):
        limiter.wait()
        print(f"  Call {i+1} at {time.perf_counter() - start_time:.3f}s")
    
    total_time = time.perf_counter() - start_time
    print(f"\nTotal time: {total_time:.3f}s (expected ~2s for 10 calls at 5/sec)")


# ============================================================================
# Example 5: Timeout Pattern
# ============================================================================

def timeout_example():
    """Implement timeout for operations."""
    print("\n=== Timeout Pattern ===\n")
    
    def wait_for_condition(timeout=5.0):
        """Wait for random condition with timeout."""
        deadline = time.monotonic() + timeout
        
        while time.monotonic() < deadline:
            # Simulate checking a condition
            if random.random() > 0.95:
                return True, "Condition met!"
            
            time.sleep(0.1)  # Check every 100ms
        
        return False, "Timeout reached"
    
    # Try with short timeout
    print("Waiting for condition (3s timeout)...")
    start = time.perf_counter()
    success, message = wait_for_condition(timeout=3.0)
    elapsed = time.perf_counter() - start
    
    print(f"Result: {message}")
    print(f"Time taken: {elapsed:.2f}s")


# ============================================================================
# Example 6: Retry with Exponential Backoff
# ============================================================================

def retry_example():
    """Implement retry logic with exponential backoff."""
    print("\n=== Retry with Backoff ===\n")
    
    def unreliable_operation():
        """Simulates unreliable operation (70% failure rate)."""
        if random.random() < 0.7:
            raise ConnectionError("Operation failed")
        return "Success!"
    
    def retry_with_backoff(func, max_retries=5, base_delay=0.1):
        """Retry with exponential backoff."""
        for attempt in range(max_retries):
            try:
                result = func()
                print(f"✓ Succeeded on attempt {attempt + 1}")
                return result
            except Exception as e:
                if attempt == max_retries - 1:
                    print(f"✗ Failed after {max_retries} attempts")
                    raise
                
                delay = base_delay * (2 ** attempt)
                print(f"  Attempt {attempt + 1} failed, retrying in {delay:.2f}s...")
                time.sleep(delay)
    
    # Test retry logic
    try:
        result = retry_with_backoff(unreliable_operation)
        print(f"Final result: {result}")
    except Exception as e:
        print(f"Operation failed: {e}")


# ============================================================================
# Example 7: Timing Context Manager
# ============================================================================

@contextmanager
def timer(label="Operation"):
    """Context manager for timing code blocks."""
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label}: {elapsed:.4f}s")


def context_manager_example():
    """Use timing context manager."""
    print("\n=== Timing Context Manager ===\n")
    
    with timer("List comprehension"):
        result = [i**2 for i in range(100000)]
    
    with timer("Generator expression"):
        result = sum(i**2 for i in range(100000))
    
    with timer("Database query simulation"):
        time.sleep(0.25)
        data = list(range(1000))


# ============================================================================
# Example 8: Time Conversion
# ============================================================================

def conversion_example():
    """Convert between time formats."""
    print("\n=== Time Conversion ===\n")
    
    # Current timestamp
    timestamp = time.time()
    print(f"Timestamp: {timestamp}")
    
    # Convert to struct_time (local)
    local_time = time.localtime(timestamp)
    print(f"\nLocal time:")
    print(f"  Year: {local_time.tm_year}")
    print(f"  Month: {local_time.tm_mon}")
    print(f"  Day: {local_time.tm_mday}")
    print(f"  Hour: {local_time.tm_hour}")
    print(f"  Minute: {local_time.tm_min}")
    
    # Convert to UTC
    utc_time = time.gmtime(timestamp)
    print(f"\nUTC time: {time.strftime('%Y-%m-%d %H:%M:%S', utc_time)}")
    
    # Format time string
    formatted = time.strftime('%A, %B %d, %Y at %I:%M %p', local_time)
    print(f"Formatted: {formatted}")
    
    # Convert back to timestamp
    reconstructed = time.mktime(local_time)
    print(f"\nReconstructed timestamp: {reconstructed}")


# ============================================================================
# Example 9: Polling Loop
# ============================================================================

def polling_example():
    """Implement a polling loop."""
    print("\n=== Polling Loop ===\n")
    
    def check_status():
        """Simulate status check."""
        return random.random() > 0.8
    
    print("Polling for status change (max 5 seconds)...")
    start = time.monotonic()
    timeout = 5.0
    poll_interval = 0.5
    
    while time.monotonic() - start < timeout:
        if check_status():
            elapsed = time.monotonic() - start
            print(f"✓ Status changed after {elapsed:.2f}s")
            break
        
        time.sleep(poll_interval)
    else:
        print("✗ Timeout: status did not change")


# ============================================================================
# Example 10: Performance Comparison
# ============================================================================

def performance_comparison():
    """Compare different time measurement methods."""
    print("\n=== Time Measurement Comparison ===\n")
    
    # Check resolution
    print("Timer resolutions:")
    print(f"  time.time(): {time.get_clock_info('time').resolution:.9f}s")
    print(f"  time.perf_counter(): {time.get_clock_info('perf_counter').resolution:.9f}s")
    print(f"  time.monotonic(): {time.get_clock_info('monotonic').resolution:.9f}s")
    
    # Measure short operation
    operation = lambda: sum(range(10000))
    
    print("\nMeasuring short operation:")
    
    # Using time.time()
    start = time.time()
    operation()
    time_elapsed = time.time() - start
    print(f"  time.time(): {time_elapsed:.9f}s")
    
    # Using perf_counter()
    start = time.perf_counter()
    operation()
    perf_elapsed = time.perf_counter() - start
    print(f"  perf_counter(): {perf_elapsed:.9f}s (RECOMMENDED)")


# ============================================================================
# Run all examples
# ============================================================================

if __name__ == '__main__':
    basic_time_example()
    benchmark_example()
    sleep_example()
    rate_limiting_example()
    timeout_example()
    retry_example()
    context_manager_example()
    conversion_example()
    polling_example()
    performance_comparison()
    
    print("\n" + "="*60)
    print("All examples completed!")
    print("="*60)
