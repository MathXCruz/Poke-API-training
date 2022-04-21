from typing import List
from poke_api.data_types import PokeSchema
import sqlalchemy
from sqlalchemy.orm import Session


def connect_to_database() -> Session:
    """Connect to the database.

    Returns:
        Session: The session to the database.
    """
    engine = sqlalchemy.create_engine(
        'sqlite:////home/matheus/Poke_API/poke_api_training.db'
    )
    session = Session(engine)
    return session


def append_all(session: Session, pkmn: List[PokeSchema]) -> None:
    """Append all the pokemon to the database.

    Args:
        session (Session): The session to the database.
        pkmn (List[PokeSchema]): The list of all the pokemon data.
    """
    for p in pkmn:
        session.add(p)
    session.commit()
    session.close()
