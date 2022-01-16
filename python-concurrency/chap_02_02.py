
"""
Section 2
Parallelism with Multiprocessing - multiprocessing(1) - Join, is_alive

Keyword - multiprocessing, processing state

"""

from multiprocessing import Process
import time
import logging



def proc_func(name: str) -> None:
    print("Subprocess {} START".format(name))
    time.sleep(3)
    print("Subprocess {} END".format(name))
    


def main() -> None:
    p = Process(target=proc_func, args=('First',))
    
    logging.info("BEFORE START SUBPROCESS")
    logging.info("Process p: %s", p)
    p.start() # Start child process
    logging.info("WAIT SUBPROCESS")
    logging.info("Process p: %s", p)
    logging.info("STATE of Process p: %s", p.is_alive())
    
    time.sleep(1)
    
    p.terminate() # Terminate process; sends SIGTERM signal or uses TerminateProcess()
    logging.info("TERMINATE SUBPROCESS")
    logging.info("Process p: %s", p)
    
    p.join()  # Wait until child process terminates
    logging.info("SUBPROCESS FINISHED")
    
    logging.info("Process p: %s", p)
    logging.info("STATE of Process p: %s", p.is_alive())

if __name__ == '__main__':
    # logging configuration
    logging.basicConfig(format="%(asctime)s - %(processName)s - %(message)s",
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
    main()
