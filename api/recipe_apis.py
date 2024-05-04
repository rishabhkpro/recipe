from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.recipe import Recipe
from datetime import datetime

from dtos.recipe_dto import (
    RecipePostRequestDto,
    RecipePostResponseBodyDto,
    RecipeResponseDto,
    RecipeGetResponse,
    RecipesGetResponse,
    RecipeDto,
    SuccessResponse,
    RecipePatchRequestDto,
)

router = APIRouter(
    prefix="/recipes",
    tags=["recipeAPIs"],
)


@router.post(
    "/create",
    status_code=201,
    response_model=RecipePostResponseBodyDto,
)
async def create_recipe(
    request_body: RecipePostRequestDto,
    db: Session = Depends(get_db),
):
    recipe_data = Recipe(
        recipe_name=request_body.recipe_name,
        recipe_type=request_body.recipe_type,
        recipe_cuisine=request_body.recipe_cuisine.title(),
        recipe_description=request_body.recipe_description,
        created_at=datetime.now(),
    )
    db.add(recipe_data)
    db.flush()
    db.commit()
    recipe = RecipeResponseDto(
        recipe_id=recipe_data.id,
        recipe_name=request_body.recipe_name,
        recipe_type=request_body.recipe_type,
        recipe_cuisine=request_body.recipe_cuisine.title(),
        recipe_description=request_body.recipe_description,
    )
    return RecipePostResponseBodyDto(body=recipe, msg="Recipe created successfully")


@router.get("", status_code=200, response_model=RecipesGetResponse)
async def get_recipes(
    db: Session = Depends(get_db),
):
    recipes = []
    all_recipes = db.query(Recipe).all()
    for recipe in all_recipes:
        temp_recipe = RecipeResponseDto(
            recipe_id=recipe.id,
            recipe_name=recipe.recipe_name,
            recipe_type=recipe.recipe_type,
            recipe_cuisine=recipe.recipe_cuisine,
            recipe_description=recipe.recipe_description,
        )
        recipes.append(temp_recipe)
    return RecipesGetResponse(body=recipes, msg="Success")


@router.get("/{recipe_id}", status_code=200, response_model=RecipeGetResponse)
async def get_recipe(
    recipe_id: int,
    db: Session = Depends(get_db),
):
    recipe = db.query(Recipe).filter().first()

    recipe_data = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe_data:
        raise HTTPException(status_code=400, detail="Recipe not found")
    recipe = RecipeResponseDto(
        recipe_id=recipe_data.id,
        recipe_name=recipe_data.recipe_name,
        recipe_type=recipe_data.recipe_type,
        recipe_cuisine=recipe_data.recipe_cuisine,
        recipe_description=recipe_data.recipe_description,
    )
    return RecipeGetResponse(body=recipe, msg="Success")


@router.patch("/{recipe_id}", status_code=200, response_model=SuccessResponse)
async def update_recipe(
    recipe_id: int,
    request_body: RecipePatchRequestDto,
    db: Session = Depends(get_db),
):

    recipe_data = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe_data:
        raise HTTPException(status_code=400, detail="Recipe details not found")

    if request_body.recipe_cuisine:
        recipe_data.recipe_cuisine = request_body.recipe_cuisine
    if request_body.recipe_type:
        recipe_data.recipe_type = request_body.recipe_type
    if request_body.recipe_description:
        recipe_data.recipe_description = request_body.recipe_description
    recipe_data.updated_at = datetime.now()

    db.commit()

    recipe = RecipeResponseDto(
        recipe_id=recipe_data.id,
        recipe_name=recipe_data.recipe_name,
        recipe_type=recipe_data.recipe_type,
        recipe_cuisine=recipe_data.recipe_cuisine,
        recipe_description=recipe_data.recipe_description,
    )

    return RecipePostResponseBodyDto(body=recipe, msg="Recipe updated successfully")


@router.delete("/{recipe_id}", status_code=200, response_model=SuccessResponse)
async def delete_recipe(
    recipe_id: int,
    db: Session = Depends(get_db),
):
    recipe_data = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe_data:
        raise HTTPException(status_code=400, detail="Recipe details not found")

    db.delete(recipe_data)
    db.commit()
    return SuccessResponse(msg="Recipe deleted successfully")
