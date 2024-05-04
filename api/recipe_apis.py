from fastapi import APIRouter

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
):
    recipe = RecipeResponseDto(
        recipe_id=1,
        recipe_name="temp",
        recipe_type="veg",
        recipe_cuisine="Indian",
        recipe_description="asdsd",
    )
    return RecipePostResponseBodyDto(body=recipe, msg="Recipe created successfully")


@router.get("", status_code=200, response_model=RecipesGetResponse)
async def get_recipes():
    recipe = RecipeResponseDto(
        recipe_id=1,
        recipe_name="temp",
        recipe_type="veg",
        recipe_cuisine="Indian",
        recipe_description="asdsd",
    )
    return RecipesGetResponse(body=[recipe], msg="Success")


@router.get("/{recipe_id}", status_code=200, response_model=RecipeGetResponse)
async def get_recipe(recipe_id: int):
    recipe = RecipeResponseDto(
        recipe_id=1,
        recipe_name="temp",
        recipe_type="veg",
        recipe_cuisine="Indian",
        recipe_description="asdsd",
    )
    return RecipeGetResponse(body=recipe, msg="Recipe created successfully")


@router.patch("/{recipe_id}", status_code=200, response_model=SuccessResponse)
async def update_recipe(recipe_id: int, request_body: RecipePatchRequestDto):
    recipe = RecipeResponseDto(
        recipe_id=1,
        recipe_name="temp",
        recipe_type="veg",
        recipe_cuisine="Indian",
        recipe_description="asdsd",
    )
    return RecipePostResponseBodyDto(body=recipe, msg="Recipe updated successfully")


@router.delete("/{recipe_id}", status_code=200, response_model=SuccessResponse)
async def delete_recipe(recipe_id: int):
    return SuccessResponse(msg="Recipe deleted successfully")
