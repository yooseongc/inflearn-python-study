
"""
Section 2
Parallelism with Multiprocessing - multiprocessing(2) - Naming 

Keyword - Naming, parallel processing

"""

# from multiprocessing import Process, current_process
from typing import List
import os
from multiprocessing import Process, current_process
import random
import time


def square(n: int) -> int:
    time.sleep(random.randint(1, 10))
    ppid = os.getppid()
    pid = os.getpid()
    pname = current_process().name
    result = n * n
    print(f"ppid: {ppid}, pid: {pid}, pname: {pname}, result: {result}")
    return result


def main() -> None:
    parent_pid = os.getppid()
    pid = os.getpid()
    print(f"ppid={parent_pid}, pid={pid}")
    
    processes: List[Process] = list()
    for i in range(1, 201):
        t = Process(name=str(i), target=square, args=(i, ))
        processes.append(t)
        t.start()
    
    for process in processes:
        process.join()
    
    print("main process finished.")
    

if __name__ == '__main__':
    main()
