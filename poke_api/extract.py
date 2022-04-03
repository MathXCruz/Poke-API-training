import requests


def get_pokeapi_data(endpoint: str, id_or_name: str) -> dict:
    """Return a dictionary of the PokeAPI data.

    Args:
        endpoint (str): The endpoint to query, endpoints can be found on
        https://pokeapi.co/docs/v2.
        id_or_name (str): The id or name of the PokeThing you want data for.

    Returns:
        dict: _description_
    """
    url = f'https://pokeapi.co/api/v2/{endpoint}/{id_or_name}'
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        return None
