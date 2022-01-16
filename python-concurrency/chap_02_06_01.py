
"""
Section 2
Parallelism with Multiprocessing - multiprocessing(5) - Queue, Pipe

Keyword - Queue, Pipe, Communications between processes

"""


from multiprocessing import Process, current_process, Queue
import os
import time
from typing import List


# Queue

def worker(baseNum: int, q: Queue):
    pid = os.getpid()
    print(f"process {current_process().name} - pid: {pid}")
    sub_total = 0
    for _ in range(baseNum):
        sub_total += 1
    
    q.put(sub_total)
    print(f"process {current_process().name} - result: {sub_total}")


def main() -> None:
    pid = os.getpid()
    print(f"main pid: {pid}")
    
    processes: List[Process] = list()
    
    st = time.time()
    
    q = Queue()
    
    for i in range(5):
        t = Process(name=str(i), target=worker, args=(100000000, q))
        processes.append(t)
        t.start()
    
    for process in processes:
        process.join()
        
    print(f"--- {time.time() - st} seconds ---")
    q.put("exit")
    
    total = 0
    while True:
        qget = q.get()
        if qget == "exit":
            break
        else:
            total += qget
    
    print(f"--- value: {total} ---")

if __name__ == '__main__':
    main()
