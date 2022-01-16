
"""
Section 3
Concurrency, CPU Bound vs I/O Bound - CPU Bound(2) - Multiprocessing

Keyword - CPU Bound

"""

import os
import time
from typing import List
from multiprocessing import current_process, Manager, Process


def cpu_bound(number: int, total_list: list) -> None:
    """1부터 number까지의 제곱의 합"""
    
    pid = os.getpid()
    pname = current_process().name
    print(f"pid: {pid}, pname: {pname}")
    total_list.append(sum(i * i for i in range(1, number + 1)))
    

def main() -> None:
    
    numbers = [3_000_000 + x for x in range(30)]
    
    procs: List[Process] = list()
    manager = Manager()
    total_list = manager.list()
    
    st = time.time()
    
    for i in numbers:
        t = Process(name=str(i), target=cpu_bound, args=(i, total_list))
        procs.append(t)
        t.start()
    
    for p in procs:
        p.join()
    
    print(f"total list: {total_list}")
    print(f"total sum: {sum(total_list)}")
    print(f"elapsed time: {time.time() - st} seconds")


if __name__ == "__main__":
    main()
