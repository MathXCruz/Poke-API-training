import pytest as pt
from poke_api.extract import get_data
from poke_api.transform import summarize, parse_dict
from poke_api import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_summarize():
    assert (
        summarize(get_data('pokemon', '1'))
        == 'Bulbasaur (ID: 1) is a grass/poison type with a weight of 6.90Kg and a height of 0.70m. It looks like this: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png'
    )
