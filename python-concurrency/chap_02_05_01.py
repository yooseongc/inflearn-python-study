
"""
Section 2
Parallelism with Multiprocessing - multiprocessing(4) - Sharing state

Keyword - memory sharing, array, value

"""

from multiprocessing import Process, current_process
import os
from typing import List


# 프로세스 메모리 공유 예제(공유X)


def generate_update_number(v: int) -> None:
    for _ in range(50):
        v += 1
    print(os.getpid(), current_process().name, "data", v)


def main() -> None:
    print(f"main pid: {os.getpid()}")
    processes: List[Process] = list()
    share_value = 0
    for _ in range(1, 11):
        p = Process(target=generate_update_number, args=(share_value, ))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
        
    print(f"share_value: ", share_value)


if __name__ == '__main__':
    main()
