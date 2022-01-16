"""
Section 1
Multithreading - Thread(5) - Producer and Consumer Using Queue
Keyword - 생산자 소비자 패턴(Producer/Consumer Pattern)

"""
"""

Producer-Consumer Pattern
(1).멀티스레드 디자인 패턴의 정석
(2).서버측 프로그래밍의 핵심
(3).주로 허리역할 중요

Python Event 객체
(1). Flag 초기값(0)
(2). Set() -> 1, Clear() -> 0, Wait(1 -> 리턴, 0 -> 대기), isSet() -> 현 플래그 상태

"""

import concurrent.futures
import logging
import queue
import random
import threading
import time


def producer(queue: queue.Queue, event: threading.Event) -> None:
    logging.info("Producer started.")
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info("Produce message: %s", message)
        queue.put(message)
        time.sleep(random.random() * 2)
    logging.info("Producer finished.")


def consumer(queue: queue.Queue, event: threading.Event):
    logging.info("Consumer started.")
    while not event.is_set():
        if queue.empty():
            logging.info("queue is empty!")
            time.sleep(1)
        else:
            message = queue.get()
            logging.info("Consume message: %s, (left queue size: %d)", message, queue.qsize())
            time.sleep(1)

    logging.info("Consumer finished.")

# Main Thread
if __name__ == "__main__":
    # logging configuration
    logging.basicConfig(format="%(asctime)s - %(threadName)s - %(message)s",
                        level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    pipeline = queue.Queue(maxsize=10)
    
    # Events manage a flag that can be set to true with the set() method 
    #     and reset to false with the clear() method. 
    # The wait() method blocks until the flag is true. The flag is initially false.
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(10)
        
        # 프로그램 종료
        event.set()

    