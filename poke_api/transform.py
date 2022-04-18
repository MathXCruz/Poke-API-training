from typing import List
from poke_api.data_types import PokeSchema

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

# transformar num objeto do sqlalchemy e fazer o append_all