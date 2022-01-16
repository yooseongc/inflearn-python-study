
"""
Section 3
Concurrency, CPU Bound vs I/O Bound - CPU Bound(1) - Synchronous

Keyword - CPU Bound

"""

import time
from typing import List

def cpu_bound(number: int) -> int:
    """1부터 number까지의 제곱의 합"""
    return sum(i * i for i in range(1, number + 1))


def find_sums(numbers: List[int]) -> List[int]:
    result = []
    for number in numbers:
        result.append(cpu_bound(number))
    return result


def main() -> None:
    numbers = [3_000_000 + x for x in range(30)]
    
    st = time.time()
    
    total = find_sums(numbers)
    
    print(f"total sum: {sum(total)}")
    print(f"elapsed time: {time.time() - st} seconds")


if __name__ == "__main__":
    main()
