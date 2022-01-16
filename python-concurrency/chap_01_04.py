"""
Section 1
Multithreading - Thread(2) - Daemon, Join
Keyword - DeamonThread, Join

"""
"""

DaemonThread(데몬스레드)
(1).백그라운드에서 실행
(2).메인스레드 종료시 즉시 종료
(3).주로 백그라운드 무한 대기 시 이벤트 발생시 실행하는 부분 담당
(4).일반 스레드는 작업 종료시 까지 실행

"""

import logging
import threading


# Thread Function
def thread_func(name: str, d: range) -> None:
    logging.info("STARTED with argument (name=%s).", name)
    for i in d:
        if i % 1000 == 0: 
            print(i)
    logging.info("FINISHED.")


# Main Thread
if __name__ == "__main__":
    # logging configuration
    logging.basicConfig(format="%(asctime)s - %(threadName)s - %(message)s",
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("STARTED.")
    
    # create threads
    x = threading.Thread(target=thread_func, args=('First', range(20000)), daemon=True)
    logging.info("CREATED thread(%s).", x)    
    y = threading.Thread(target=thread_func, args=('Second', range(10000)), daemon=True)    
    logging.info("CREATED thread(%s).", y)
    
    # run threads
    x.start()
    y.start()
    
    # Wait until the thread terminates.
    # x.join()
    # y.join()
    
    logging.info("Main Thread DONE.")
