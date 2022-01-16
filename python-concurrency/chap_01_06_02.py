"""
Section 1
Multithreading - Thread(4) - Lock, Deadlock
Keyword - Lock, Deadlock, Race Condition, Thread synchronization

"""
"""

용어 설명
(1).세마포어(Semaphore) : 프로세스간 공유된 자원에 접근 시 문제 발생 가능성 
    -> 한 개의 프로세스만 접근 처리 고안(경쟁상태 예방)
(2).뮤텍스(Mutex) : 공유된 자원의 데이터를 여러 스레드가 접근하는 것을 막는 것.-> 경쟁상태 예방
(3).Lock : 상호 배제를 위한 잠금(Lock)처리(데이터 경쟁)
(4).데드락(Deadlock) : 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황(교착상태)
(5).Thread synchronization(스레드 동기화)를 통해서 안정적으로 동작하게 처리한다.(동기화메소드, 동기화 블록)
(6).Semaphore와 Mutex의 차이점?
    -> 세마포어와 뮤텍스 개체는 모두 병렬 프로그래밍 환경에서 상호 배제를 위해 사용 
    -> 뮤텍스 개체는 단일 스레드가 리소스 또는 중요 섹션을 소비 허용
	-> 세마포어는 리소스에 대한 제한된 수의 동시 액세스를 허용

"""


import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading


class FakeDataStore:
    
    def __init__(self) -> None:
        self.value = 0    # heap variable --> shared
        self._lock = threading.Lock()
        
    def update(self, name: str) -> None:
        logging.info("Thread %s: started update store init==> %s", name, self.value)
        
        # synchronizing needed
        self._lock.acquire()
        
        logging.info("Thread %s get lock", name)
        local_copy = self.value   # copy heap value to stack (not shared by threads)
        local_copy += 1
        time.sleep(1)
        self.value = local_copy   # put stack value to heap
        
        self._lock.release()
        logging.info("Thread %s release lock", name)
        
        logging.info("Thread %s: finished update store last==> %s", name, local_copy)


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
    
    store = FakeDataStore()
    logging.info("STARTED store with initial value: %s", store.value)
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        task_names = ['First', 'Second', 'Third']
        for name in task_names:
            executor.submit(store.update, name)
    
    logging.info("FINISHED.")
    logging.info("FINISHED store with value: %s", store.value)
    

# Main Thread
if __name__ == "__main__":
    # logging configuration
    logging.basicConfig(format="%(asctime)s - %(threadName)s - %(message)s",
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    main()