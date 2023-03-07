#!/usr/bin/env python3

import asyncio
import time

async def do_something(n: int) -> int:
    for _ in range(10):
        print(f"working {n}")
        await asyncio.sleep(n/10.0)
        # time.sleep(n/10.0)
    return 1000*n + 42

def do_something_blocking(n: int) -> int:
    for _ in range(10):
        print(f"working {n}")
        time.sleep(n/10.0)
    return 1000*n + 42

async def main():
    l = await asyncio.gather(
        *(do_something(n) for n in range(20))
    )

    # l = await asyncio.gather(
    #     *(do_something_blocking(n) for n in range(20))
    # )

    # l = await asyncio.gather(
    #     *(asyncio.to_thread(do_something_blocking, n) for n in range(20))
    # )

    print(f"{l}")

    # strace shows it uses fixed number of threads (seven calls to clone3).
    # which suggests there is a thread-pool.
    # ThreadPoolExecutor?
    # In [1]: import asyncio
    # In [2]: asyncio.sleep??


if __name__ == "__main__":
    asyncio.run(main())