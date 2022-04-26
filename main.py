from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from poke_api import extract
from poke_api import transform
from poke_api import load
import asyncio
import time
import sys


async def main():
    pkmn = await extract.get_pokemon_data(1, 31)
    pkmn = transform.parse_batch(pkmn)
    pokemon = transform.types_to_string(pkmn)
    pokemon = transform.pydantic_to_orm(pokemon)
    engine = create_async_engine(
        'sqlite+aiosqlite:////home/matheus/Poke_API/poke_api_training.db'
    )
    await load.create_database(engine)
    session = sessionmaker(engine, future=True, class_=AsyncSession)
    async with session() as s:
        s.add_all(pokemon)
        await s.commit()


def sync_main():
    pkmn = extract.get_pokemon_data_sync(1, 3)
    pkmn = transform.parse_batch(pkmn)
    pokemon = transform.types_to_string(pkmn)
    pokemon = transform.pydantic_to_orm(pokemon)
    engine = create_engine(
        'sqlite:////home/matheus/Poke_API/poke_api_training.db'
    )
    session = sessionmaker(engine, future=True, class_=Session)
    with session() as s:
        s.add_all(pokemon)
        s.commit()


if __name__ == '__main__':
    start = time.time()
    if len(sys.argv) > 1 and sys.argv[1] == '--sync':
        sync_main()
    else:
        asyncio.run(main())
    print(f'Duration: {time.time() - start} seconds')
