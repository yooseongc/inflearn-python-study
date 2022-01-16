"""
Section 1
Multithreading - Thread(1) - Basic
Keyword - threading basic

"""
import logging
import threading
import time


# Thread 1 Function
def thread_func_1(name: str) -> None:
    logging.info("STARTED with argument (name=%s).", name)
    time.sleep(3)
    logging.info("FINISHED.")


# Main Thread
if __name__ == "__main__":
    # logging configuration
    logging.basicConfig(format="%(asctime)s - %(threadName)s - %(message)s",
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("STARTED.")
    
    # create thread 1
    x = threading.Thread(target=thread_func_1, args=('First',))    
    logging.info("CREATED thread 1(%s).", x)
    
    # run thread 1
    x.start()
    
    # Wait until the thread terminates.
    logging.info("WAITING thread 1(%s).", x)
    x.join()
    
    logging.info("DONE thread 1(%s).", x)
    