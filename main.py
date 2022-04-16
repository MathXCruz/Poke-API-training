from poke_api.extract import get_async_data, get_sync_data
import asyncio
import time


async def main():
    pkmn = await get_async_data()
    print(pkmn)

def sync_main():
    pkmn = get_sync_data()
    print(pkmn)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    #sync_main()
    print(f'Duration: {time.time() - start} seconds')