from typing import List
from poke_api.data_types import PokeSchema
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine


def connect_to_database_sync() -> Session:
    """Connect to the database synchronously.

    Returns:
        Session: The sync session to the database.
    """
    engine = create_engine(
        'sqlite:////home/matheus/Poke_API/poke_api_training.db'
    )
    session = sessionmaker(engine, future=True, class_=Session)
    return session


async def connect_to_database() -> AsyncSession:
    """Connect to the database.

    Returns:
        Session: The session to the database.
    """
    engine = create_async_engine(
        'sqlite+aiosqlite:////home/matheus/Poke_API/poke_api_training.db'
    )
    session = sessionmaker(engine, future=True, class_=AsyncSession)
    return session


def append_all_sync(session: Session, pkmn: List[PokeSchema]) -> None:
    """Append all the pokemon to the database synchronously.

    Args:
        session (Session): The sync session to the database.
        pkmn (List[PokeSchema]): The list of all the pokemon data.
    """
    with session() as s:
        for p in pkmn:
            s.add(p)
        s.commit()


async def append_all(session: AsyncSession, pkmn: List[PokeSchema]) -> None:
    """Append all the pokemon to the database.

    Args:
        session (AsyncSession): The session to the database.
        pkmn (List[PokeSchema]): The list of all the pokemon data.
    """
    async with session() as s:
        for p in pkmn:
            s.add(p)
        await s.commit()
