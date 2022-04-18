from pydantic import BaseModel, Field
from typing import List


class PokeSchema(BaseModel):
    id: int = Field(gt=0, description="ID of the pokemon")
    name: str = Field(description="Name of the pokemon")
    types: List[str] = Field(min_items=1, max_items=2, description="Types of the pokemon")
    weight: float = Field(gt=0, description="Weight of the pokemon")
    height: float = Field(gt=0, description="Height of the pokemon")
    sprite: str = Field(description="Link to the sprite of the pokemon")