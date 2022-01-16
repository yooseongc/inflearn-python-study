"""
Section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(2) - threading vs asyncio vs multiprocessing


Keyword - I/O Bound, requests, threading

"""

from typing import List
import multiprocessing
import requests
import time

session: requests.Session = None

def set_global_session() -> None:
    global session
    if not session:
        session = requests.Session()


def request_site(url: str) -> None:
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name} - {session}")
        print(f"{name} - [Read Contents : {len(response.content)}, Status Code : {response.status_code}] from {url}")
        

def request_all_site(urls: List[str]) -> None:
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool:
        pool.map(request_site, urls)


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
    