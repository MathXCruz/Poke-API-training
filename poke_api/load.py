from poke_api.data_types import Base
from sqlalchemy.ext.asyncio import AsyncEngine


async def create_database(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
