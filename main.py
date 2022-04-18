from poke_api import extract
from poke_api import transform
from poke_api import load
import asyncio
import time


async def main():
    pkmn = await extract.run_all()
    #pkmn = transform.parse_batch(pkmn)
    print(pkmn)

def sync_main():
    pkmn = extract.get_sync_data()
    print(pkmn)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    #sync_main()
    print(f'Duration: {time.time() - start} seconds')
