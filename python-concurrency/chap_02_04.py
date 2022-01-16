
"""
Section 2
Parallelism with Multiprocessing - multiprocessing(3) - ProcessPoolExecutor

Keyword - ProcessPoolExecutor, as_completed, futures, timeout, dict

"""

from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Any
import urllib.request



URLS = [
    'http://www.daum.net/',
    'http://www.cnn.com/',
    'https://en.wikipedia.org/wiki/Parent_process',
    'http://www.bbc.co.uk/',
    'http://naver.com/'
]


def load_url(url: str, timeout: float) -> Any:
    with urllib.request.urlopen(url, timeout=timeout) as resp:
        return resp.read()


def main() -> None:
    with ProcessPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print("%r generated an exception: %s" % (url, exc))
            else:
                print("%r page is %d bytes" % (url, len(data)))


if __name__ == '__main__':
    main()
