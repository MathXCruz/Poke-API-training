from poke_api import extract
from poke_api import transform
from poke_api import load
import asyncio
import time
import sys


async def main():
    pkmn = await extract.get_pokemon_data(1, 81)
    pkmn = transform.parse_batch(pkmn)
    pkmn = transform.pydantic_to_orm(pkmn)
    session = await load.connect_to_database()
    await load.append_all(session, pkmn)


def sync_main():
    pkmn = extract.get_data_sync(1, 81)
    pkmn = transform.parse_batch(pkmn)
    pkmn = transform.pydantic_to_orm(pkmn)
    session = load.connect_to_database_sync()
    load.append_all_sync(session, pkmn)


if __name__ == '__main__':
    start = time.time()
    if len(sys.argv) > 1 and sys.argv[1] == '--sync':
        sync_main()
    else:
        asyncio.run(main())
    print(f'Duration: {time.time() - start} seconds')
