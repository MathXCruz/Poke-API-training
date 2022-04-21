from pydantic import BaseModel, Field
from typing import List
from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import declarative_base


class PokeSchema(BaseModel):
    id: int = Field(gt=0, description="ID of the pokemon")
    name: str = Field(description="Name of the pokemon")
    types: List[str] = Field(min_items=1, max_items=2, description="Types of the pokemon")
    weight: float = Field(gt=0, description="Weight of the pokemon")
    height: float = Field(gt=0, description="Height of the pokemon")
    sprite: str = Field(description="Link to the sprite of the pokemon")

Base = declarative_base()

class PokeORM(Base):
    __tablename__ = 'pokemon'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    types = Column(Text(), nullable=False)
    weight = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    sprite = Column(String(255), nullable=False)