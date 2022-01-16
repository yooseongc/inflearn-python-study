"""
Section 1
Multithreading - Thread(3) - ThreadPoolExecutor
Keyword - Many Threads, concurrent.futures, (xxx)PoolExcutor

"""
"""

그룹스레드
(1).Python 3.2 이상 표준 라이브러리 사용
(2).concurrent.futures
(3).with사용으로 생성, 소멸 라이프사이클 관리 용이
(4).디버깅하기가 난해함(단점)
(5).대기중인 작업 -> Queue -> 완료 상태 조사 -> 결과 또는 예외 -> 단일화(캡슐화)

"""


import logging
from concurrent.futures import ThreadPoolExecutor


# Thread Function
def task(name: str) -> int:
    logging.info("STARTED with argument (name=%s).", name)
    
    result = 0
    for i in range(1, 100001):
        result = result + i
        
    logging.info("FINISHED with result (%s).", result)
    return result


def main() -> None:
    logging.info("STARTED.")
    
    executor = ThreadPoolExecutor(max_workers=3)
    task1 = executor.submit(task, ('First', ))
    task2 = executor.submit(task, ('Second', ))
    
    # Return the result of the call that the future represents.
    # Args:
    #    timeout: The number of seconds to wait for the result if the future
    #        isn't done. If None, then there is no limit on the wait time.
    logging.info("task1 result= %s", task1.result())
    logging.info("task2 result= %s", task2.result())
    
    logging.info("FINISHED.")
    

# Main Thread
if __name__ == "__main__":
    # logging configuration
    logging.basicConfig(format="%(asctime)s - %(threadName)s - %(message)s",
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    main()