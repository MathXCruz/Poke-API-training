from poke_api import extract
from poke_api import transform
from poke_api import load
import asyncio
import time


async def main():
    pkmn = await extract.get_async_data()
    print(pkmn)


def sync_main():
    pkmn = extract.get_sync_data()
    print(pkmn)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    # sync_main()
    print(f'Duration: {time.time() - start} seconds')
