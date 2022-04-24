from typing import List
from poke_api.data_types import PokeSchema, PokeORM


def summarize(pokemon: dict) -> str:
    """Return a string of the summary of the pokemon.

    Args:
        pokemon (dict): The dictionary of the pokemon data.

    Returns:
        str: Summarized pokemon info.
    """
    p = parse_dict(pokemon)
    return f'{p.name.title()} (ID: {p.id}) is a {"/".join(map(str, p.types))} type with \
a weight of {p.weight:.2f}Kg and a height of {p.height:.2f}m. It looks like \
this: {p.sprite}'


def parse_dict(pokemon: dict) -> PokeSchema:
    """Return the parsed data of the pokemon.

    Args:
        pokemon (dict): The dictionary of the pokemon data.

    Returns:
        str: The parsed data of the pokemon.
    """
    poke_dict = {
        'id': pokemon['id'],
        'name': pokemon['name'],
        'types': [poke['type']['name'] for poke in pokemon['types']],
        'weight': pokemon['weight'] / 10,
        'height': pokemon['height'] / 10,
        'sprite': pokemon['sprites']['front_default'],
    }
    return PokeSchema(**poke_dict)


def parse_batch(pokemon: List[dict]) -> List[PokeSchema]:
    """Return the parsed data of all the pokemon.

    Args:
        pokemon (List[dict]): The list of all the pokemon data.

    Returns:
        List[PokeSchema]: The parsed data of all the pokemon.
    """
    return [parse_dict(p) for p in pokemon]


def pydantic_to_orm(pokemon: List[PokeSchema]) -> List[PokeORM]:
    """Convert the pydantic data to the ORM data.

    Args:
        pokemon (List[PokeSchema]): The list of all the pokemon data.

    Returns:
        List[PokeORM]: The list of all the pokemon data converted
         to the ORM format.
    """
    poke = []
    types_to_string(pokemon)
    [
        poke.append(
            PokeORM(
                id=p.id,
                name=p.name,
                types=p.types,
                weight=p.weight,
                height=p.height,
                sprite=p.sprite,
            )
        )
        for p in pokemon
    ]
    return poke


def types_to_string(pokemon: List[PokeSchema]) -> List[PokeSchema]:
    """Convert the types of the pokemon to a comma separated string.

    Args:
        pokemon (List[PokeSchema]): The list of all the pokemon data.

    Returns:
        List[PokeSchema]: The list of all the pokemon data with the
        types as a string.
    """
    for p in pokemon:
        p.types = ', '.join(p.types)
    return pokemon
