"""
Section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(2) - threading vs asyncio vs multiprocessing


Keyword - I/O Bound, requests, threading

"""

from typing import List
import concurrent.futures
import threading
import requests
import time


# 각 스레드에 생성되는 객체(독립적)
thread_local = threading.local()


def get_session() -> requests.Session:
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def request_site(url: str) -> None:
    session = get_session()
    with session.get(url) as response:
        print(f"[Read Contents : {len(response.content)}, Status Code : {response.status_code}] from {url}")
        

def request_all_site(urls: List[str]) -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(request_site, urls)


def main() -> None:
    urls = [
            "https://www.jython.org",
            "http://olympus.realpython.org/dice",
            "https://realpython.com/"
    ] * 3
    
    # 실행시간 측정
    start_time = time.time()

    # 실행
    request_all_site(urls)

    # 실행 시간 종료
    duration = time.time() - start_time

    # 결과 출력
    print(f"Downloaded {len(urls)} sites in {duration} seconds.")


if __name__ == "__main__":
    main()
    