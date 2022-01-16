
"""
Section 2
Parallelism with Multiprocessing - multiprocessing(5) - Queue, Pipe

Keyword - Queue, Pipe, Communications between processes

"""


from multiprocessing import Process, current_process, Pipe
from multiprocessing.connection import Connection
import os
import time
from typing import List


# Queue

def worker(baseNum: int, conn: Connection):
    with conn:
        pid = os.getpid()
        print(f"process {current_process().name} - pid: {pid}")
        sub_total = 0
        for _ in range(baseNum):
            sub_total += 1
        
        conn.send(sub_total)
        print(f"process {current_process().name} - result: {sub_total}")


def main() -> None:
    pid = os.getpid()
    print(f"main pid: {pid}")
    
    processes: List[Process] = list()
    p_conns: List[Connection] = list()
    
    st = time.time()
    
    for i in range(5):
        parent_conn, child_conn = Pipe()
        t = Process(name=str(i), target=worker, args=(100000000, child_conn))
        processes.append(t)
        p_conns.append(parent_conn)
        t.start()
    
    for process in processes:
        process.join()
        
    print(f"--- {time.time() - st} seconds ---")
    
    total = 0
    for conn in p_conns:
        with conn:
            total += conn.recv()
    
    print(f"--- value: {total} ---")

if __name__ == '__main__':
    main()
