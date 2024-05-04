from database import Base
from typing import List, Literal
from sqlalchemy import Column, Integer, String, DateTime


class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, auto_increment=True, index=True)
    recipe_name = Column(String, unique=False, nullable=False)
    recipe_type = Column(String, nullable=False)
    recipe_cuisine = Column(String, nullable=False)
    recipe_description = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
