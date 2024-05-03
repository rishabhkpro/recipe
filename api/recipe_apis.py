from fastapi import APIRouter


router = APIRouter()


@router.post(
    "/recipes/create",
    tags=["recipeAPIs"],
)
async def create_recipe():
    return "Created recipe successfully"


@router.get(
    "/recipes",
    tags=["recipeAPIs"],
)
async def get_recipes():
    return "List of recipes"


@router.get(
    "/recipes/{recipe_id}",
    tags=["recipeAPIs"],
)
async def get_recipe():
    return "Details of recipe"


@router.patch(
    "/recipes/{recipe_id}",
    tags=["recipeAPIs"],
)
async def update_recipe():
    return "Recipe updated"


@router.delete(
    "/recipes/{recipe_id}",
    tags=["recipeAPIs"],
)
async def delete_recipe():
    return "Deleted recipe successfully"
