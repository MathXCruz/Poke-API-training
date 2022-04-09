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


def parse_dict(pokemon: dict) -> str:
    """Return the parsed data of the pokemon.

    Args:
        pokemon (dict): The dictionary of the pokemon data.

    Returns:
        str: The parsed data of the pokemon.
    """
    name = pokemon['name']
    id = pokemon['id']
    types = [poke['type']['name'] for poke in pokemon['types']]
    sprite = pokemon['sprites']['front_default']
    weight = pokemon['weight'] * 0.1
    height = pokemon['height'] * 0.1
    return name, id, types, sprite, weight, height
