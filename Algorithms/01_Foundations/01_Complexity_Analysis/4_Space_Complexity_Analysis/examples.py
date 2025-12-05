"""Runnable space-complexity demos for B.1 Foundations/4 Space Complexity Analysis.

Each function mirrors a scenario from the README so learners can
observe auxiliary-space trade-offs directly from the terminal.
"""

from __future__ import annotations

import sys
from typing import Generator, Iterable, List


def reverse_in_place(values: List[int]) -> None:
    """Reverse a list without allocating another list (O(1) auxiliary space)."""

    left, right = 0, len(values) - 1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1


def reversed_copy(values: Iterable[int]) -> List[int]:
    """Produce a reversed copy using slicing (O(n) additional space)."""

    return list(values)[::-1]


def list_vs_generator_memory(limit: int) -> tuple[int, int]:
    """Return byte sizes of a list vs generator that produce the same sequence."""

    eager = list(range(limit))
    lazy = (num for num in range(limit))
    return sys.getsizeof(eager), sys.getsizeof(lazy)


def rolling_window_sum(nums: List[int], window: int) -> List[int]:
    """Compute sliding-window sums with O(1) extra space via in-place prefix reuse."""

    if window <= 0 or window > len(nums):
        raise ValueError("window must be between 1 and len(nums)")

    # Build prefix sums in-place to avoid auxiliary array.
    for idx in range(1, len(nums)):
        nums[idx] += nums[idx - 1]

    result = []
    for right in range(window - 1, len(nums)):
        left = right - window
        window_sum = nums[right] - (nums[left] if left >= 0 else 0)
        result.append(window_sum)
    return result


def fibonacci_recursive(n: int) -> int:
    """Classic recursion that incurs O(n) stack usage."""

    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    """Iterative variant that stays O(1) in space."""

    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def main() -> None:
    numbers = [1, 2, 3, 4, 5]
    copy_version = reversed_copy(numbers)
    reverse_in_place(numbers)
    print(f"in-place reversed: {numbers}")
    print(f"copied reversed:  {copy_version}")

    list_bytes, gen_bytes = list_vs_generator_memory(10_000)
    print(f"list bytes: {list_bytes:,}")
    print(f"generator bytes: {gen_bytes:,}")

    window_input = [2, 1, 3, 4, 5, 2]
    print(f"window sums (size 3): {rolling_window_sum(window_input, 3)}")

    fib_index = 10
    print(f"fib recursive({fib_index}): {fibonacci_recursive(fib_index)}")
    print(f"fib iterative({fib_index}): {fibonacci_iterative(fib_index)}")


if __name__ == "__main__":
    main()
