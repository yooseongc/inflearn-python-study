"""
Section 3
Concurrency, CPU Bound vs I/O Bound - I/O Bound(2) - Asyncio basic
Keyword - asyncio

"""

import time
import asyncio


def calc_sync(name: str, n: int) -> None:
    for i in range(1, n + 1):
        print(f"{name} -> {i} of {n}")
        time.sleep(1)
    print(f"{name} - {n} done!")


def proc_sync():
    start = time.time()
    calc_sync('One', 1)
    calc_sync('Two', 2)
    calc_sync('Three', 3)
    end = time.time()
    
    print(f"elapsed time: {end - start} seconds")
    

async def calc_async(name: str, n: int) -> None:
    for i in range(1, n + 1):
        print(f"{name} -> {i} of {n}")
        await asyncio.sleep(1)
    print(f"{name} - {n} done!")
    
    
async def proc_async():
    start = time.time()
    t1 = asyncio.create_task(calc_async('One', 1))
    t2 = asyncio.create_task(calc_async('Two', 2))
    t3 = asyncio.create_task(calc_async('Three', 3))
    await t1
    await t2
    await t3
    end = time.time()
    
    print(f"elapsed time: {end - start} seconds")


if __name__ == "__main__":
    
    print("================= SYNC ================")
    proc_sync()
    
    print("================= ASYNC ================")
    asyncio.run(proc_async())  # Python 3.7 이상 
    # asnycio.get_event_loop().run_until_complete(proc_async())  # Python 3.7 미만 
    