![example workflow](https://github.com/MathXCruz/Poke_API_training/actions/workflows/poke_api.yml/badge.svg)    [![codecov](https://codecov.io/gh/MathXCruz/Poke_API_training/branch/main/graph/badge.svg?token=QOH5NJA7FE)](https://codecov.io/gh/MathXCruz/Poke_API_training)

# Project Design
The goal of this project is to consolidate some of the concepts that I learned in my first 6 months as a Data Science intern at Juros Baixos. \
In its implementation, I use some concepts like ETL, cohesion, modularity, typehints, docstrings, logging, async extraction, async ORM, database creation, pydantic, testing and PEP8 style. \
The package management is done using Poetry, and the code is written in Python 3.8. \
This project is an async ETL project, that extracts data from the PokeAPI and stores it in a database. Both the extraction and loading are done asynchronously. \
poke_info.py is a bonus, that extracts data about a user input Pokemon and prints out a summary of its main characteristics, along with a link to its sprite.

# How to use

Download the package and run the following command:

```poetry shell```

This will activate the environment with all the necessary dependencies.

First, to create the database:

```python database_generator.py```

Then, run the code:
    
```python main.py```

Or, if you want to run the code synchronously:

```python main.py --sync```

The program will retrieve the data from the PokeAPI and store it in the database. Currently you can choose the pokemons that will be returned by editing the arguments of get_pokemon_data or get_pokemon_data_sync on the main.py file.

For poke_info.py, first run it:

```python poke_info.py```

And then, insert the pokemon name or id, e.g.:
    
```Pikachu``` or ```25```
