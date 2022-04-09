![example workflow](https://github.com/MathXCruz/Poke_API_training/actions/workflows/poke_api.yml/badge.svg)

[![codecov](https://codecov.io/gh/MathXCruz/Poke_API_training/branch/main/graph/badge.svg?token=QOH5NJA7FE)](https://codecov.io/gh/MathXCruz/Poke_API_training)

# Project Design
The goal of this project is to consolidate some of the concepts that I learned in my first few months as a Data Science intern at Juros Baixos. \
In its implementation, I use some concepts like ETL, cohesion, modularity, typehints, docstrings, logging, testing and PEP8 style. \
The package management is done using Poetry, and the code is written in Python 3.8. \
The PokeAPI extraction function is written in a way that allows access to any endpoint of the API. \
Currently, the code extracts data about a user input Pokemon (/pokemon endpoint) and prints out a summary of its main characteristics, along with a link to its sprite.

# How to use

Download the package and run the following command:

```poetry shell```

This will activate the environment with all the necessary dependencies.

Then, run the code:
    
```python main.py```

And finally, insert the pokemon name or id, e.g.:
    
```Pikachu``` or ```25```
