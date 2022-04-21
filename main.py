from poke_api import extract
from poke_api import transform
from poke_api import load
import asyncio
import time


async def main():
    pkmn = await extract.get_pokemon_data()
    pkmn = transform.parse_batch(pkmn)
    pkmn = transform.pydantic_to_orm(pkmn)
    session = load.connect_to_database()
    load.append_all(session, pkmn)
    print(pkmn)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'Duration: {time.time() - start} seconds')
