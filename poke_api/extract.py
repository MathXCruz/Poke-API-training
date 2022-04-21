import logging
import asyncio
import httpx
from typing import List


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
    logging.debug(f'get_data(poke_api): {response.status_code}')
    return response.json()


async def get_pokemon_data() -> List[dict]:
    """Return a dictionary list of data of the Pokemon in the ID range.

    Returns:
        dict: The raw data of every requested pokemon.
    """
    reqs = [create_request(ID) for ID in range(852, 899)]
    poke_list = await get_pokemon(reqs)
    pokemon = [p.json() for p in poke_list]
    return pokemon


def create_request(ID: int) -> httpx.Request:
    """Create a get request for the given ID.

    Args:
        ID (int): The id of the pokemon you want data for.

    Returns:
        httpx.Request: The request to get the data for the pokemon.
    """
    return httpx.Request('GET', url=f'https://pokeapi.co/api/v2/pokemon/{ID}')


async def get_pokemon(reqs: List[httpx.Request]) -> List[httpx.Response]:
    """Create a client and manage the creation and execution of the requests.

    Args:
        reqs (List[httpx.Request]): A list of requests to make.

    Returns:
        List[httpx.Response]: A list of responses from the requests.
    """
    async with httpx.AsyncClient() as client:
        tasks = [client.send(req) for req in reqs]
        return await asyncio.gather(*tasks)


def get_sync_data() -> list:
    """Return a dictionary of data from the 1st to the 809th Pokemon.

    Uses Synchronous requests.

    Returns:
        list: A list containing the raw data of every requested pokemon.
    """
    pkmn = []
    with httpx.Client() as client:
        for id in range(1, 252):
            url = f'https://pokeapi.co/api/v2/pokemon/{id}'
            response = client.get(url)
            logging.debug(f'get_async_data(poke_api): {response.status_code}')
            pkmn.append(response.json())
    return pkmn
