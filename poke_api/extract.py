import logging
import asyncio
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
    logging.debug(f'get_data(poke_api): {response.status_code}')
    if response.status_code == 200:
        return response.json()
    else:
        return None


async def get_async_data(url: str, client: object) -> list:
    """Do the request for the specified pokemon.
    
    Uses Asynchronous requests.

    Returns:
        dict: The raw data of every requested pokemon.
    """
    response = await client.get(url)
    logging.debug(f'get_async_data(poke_api): {response.status_code}')
    if response.status_code == 200:
        pkmn = (response.json())
    else:
        return f'Error: {response.json()}'
    return pkmn


async def run_all():
    """Create a client and manage the creation and execution of the requests.

    Returns:
        dict: The raw data of every requested pokemon.
    """    
    pkmn = []
    async with httpx.AsyncClient() as client:
        urls = [f'https://pokeapi.co/api/v2/pokemon/{ID}' for ID in range(1, 252)]
        poke_list = await asyncio.gather(*[get_async_data(url, client) for url in urls])
        '''for ID in range(1, 252):
            url = f'https://pokeapi.co/api/v2/pokemon/{ID}'
            pkmn.append(asyncio.ensure_future(get_async_data(url, client)))
            poke_list = await asyncio.gather(*pkmn)'''
    return poke_list


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
            if response.status_code == 200:
                pkmn.append(response.json())
            else:
                return f'Error: {response.json()}'
    return pkmn
