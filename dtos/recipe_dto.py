from typing import List, Literal, Optional
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from pydantic import BaseModel, Field
from humps import camelize


def to_camel(string):
    return camelize(string)


class CamelModel(BaseModel):
    class Config:
        alias_generator = to_camel
        populate_by_name = True


class RecipeDto(CamelModel):
    recipe_name: str
    recipe_type: Literal["veg", "non-veg"]
    recipe_description: str
    recipe_cuisine: Literal["Indian", "Italian", "Chinese"]


class SuccessResponse(BaseModel):
    msg: str


class RecipePostRequestDto(RecipeDto):
    pass


class RecipePatchRequestDto(CamelModel):
    recipe_name: Optional[str]
    recipe_type: Optional[Literal["veg", "non-veg"]]
    recipe_description: Optional[str]
    recipe_cuisine: Optional[Literal["Indian", "Italian", "Chinese"]]


class RecipeResponseDto(RecipeDto):
    recipe_id: int


class RecipePostResponseBodyDto(BaseModel):
    body: RecipeResponseDto
    msg: str


class RecipeGetResponse(RecipePostResponseBodyDto):
    pass


class RecipesGetResponse(BaseModel):
    body: List[RecipeResponseDto]
    msg: str
