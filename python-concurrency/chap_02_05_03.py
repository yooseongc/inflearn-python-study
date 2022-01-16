
"""
Section 2
Parallelism with Multiprocessing - multiprocessing(4) - Sharing state

Keyword - memory sharing, array, value

"""

import array
from multiprocessing import Process, current_process, Array, Value
from multiprocessing.sharedctypes import Synchronized, SynchronizedArray
import os
from typing import Any, List


# 프로세스 메모리 공유 예제(공유O with Lock)


def generate_update_number(v: Synchronized, a: SynchronizedArray) -> None:
    with v.get_lock():
        for _ in range(50):
            v.value += 1
    with a.get_lock():
        for _ in range(50):
            a[0] = a[0] + 1
    print(os.getpid(), current_process().name, "data", v.value, a[:])


def main() -> None:
    print(f"main pid: {os.getpid()}")
    processes: List[Process] = list()
    shared_numbers = Array('i', range(3), lock=True)
    share_value = Value('i', 0, lock=True)
    
    for _ in range(1, 11):
        p = Process(target=generate_update_number, args=(share_value, shared_numbers))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
        
    print(f"share_value: ", share_value.value, shared_numbers[:])


if __name__ == '__main__':
    main()
