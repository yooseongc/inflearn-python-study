"""
Section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(2) - threading vs asyncio vs multiprocessing

Keyword - I/O Bound, requests, asyncio

"""

# threading 보다 높은 코드 복잡도 -> Async, Await 적절하게 코딩

import asyncio
from typing import Any, List
import aiohttp
import time


async def request_site(session: aiohttp.ClientSession, url: str) -> int:
    async with session.get(url) as response:
        print("Read Contents {0}, from {1}".format(response.content_length, url))
        return response.status


async def request_all_site(urls: List[str]) -> List[int]:
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)
            
        return await asyncio.gather(*tasks, return_exceptions=True)
    

def main() -> None:
    # 테스트 URLS
    urls = [
            "https://www.python.org/",
            "http://olympus.realpython.org/dice",
            "https://www.daum.net/"
    ] * 3
    
    # 실행시간 측정
    start_time = time.time()

    # 실행1
    result = asyncio.get_event_loop().run_until_complete(request_all_site(urls))
    # 실행2(파이썬 3.7 이상)
    # asyncio.run(request_all_site(urls))
    
    print(result)

    # 실행 시간 종료
    duration = time.time() - start_time

    # 결과 출력
    print(f"Downloaded {len(urls)} sites in {duration} seconds.")
    

if __name__ == "__main__":
    main()
    