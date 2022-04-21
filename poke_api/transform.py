from typing import List
from poke_api.data_types import PokeSchema, PokeORM

def summarize(pokemon: dict) -> str:
    """Return a string of the summary of the pokemon.

    Args:
        pokemon (dict): The dictionary of the pokemon data.

    Returns:
        str: Summarized pokemon info.
    """
    name, id, types, sprite, weight, height = parse_dict(pokemon)
    return f'{name.title()} (ID: {id}) is a {"/".join(map(str, types))} type with \
a weight of {weight:.2f}Kg and a height of {height:.2f}m. It looks like \
this: {sprite}'


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
        'weight': pokemon['weight']/10,
        'height': pokemon['height']/10,
        'sprite': pokemon['sprites']['front_default']
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
    poke = []
    [poke.append(PokeORM(id=p.id, name=p.name, types=p.types, weight=p.weight, height=p.height, sprite=p.sprite)) for p in pokemon]
    return poke