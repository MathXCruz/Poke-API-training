import logging
import httpx


def get_data(endpoint: str, id_or_name: str) -> dict:
    """Return a dictionary of the PokeAPI data.

    Args:
        endpoint (str): The endpoint to query, endpoints can be found on
        https://pokeapi.co/docs/v2.
        id_or_name (str): The id or name of the PokeThing you want data for.

    Returns:
        dict: _description_
    """
    url = f'https://pokeapi.co/api/v2/{endpoint}/{id_or_name}'
    response = httpx.get(url)
    logging.debug(
        f'get_data(poke_api): {response.status_code}'
    )
    if response.status_code == 200:
        return response.json()
    else:
        return None


async def get_async_data() -> dict:
    pkmn = []
    async with httpx.AsyncClient() as client:
        for id in range(1,810):
            url = f'https://pokeapi.co/api/v2/pokemon/{id}'
            response = await client.get(url)
            logging.debug(
            f'get_async_data(poke_api): {response.status_code}'
        )
            if response.status_code == 200:
                pkmn.append(response.json())
            else:
                return f'Error: {response.json()}'
    return pkmn

def get_sync_data() -> dict:
    pkmn = []
    with httpx.Client() as client:
        for id in range(1, 810):
            url = f'https://pokeapi.co/api/v2/pokemon/{id}'
            response = client.get(url)
            logging.debug(
            f'get_async_data(poke_api): {response.status_code}'
        )
            if response.status_code == 200:
                pkmn.append(response.json())
            else:
                return f'Error: {response.json()}'
    return pkmn