from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from fastapi import status

from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from app import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"


def get_override_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


app.dependency_overrides[get_db] = get_override_db


client = TestClient(app)


def test_get_recipes_returns_zero_recipes():
    recipe_res = client.get(
        "/recipes",
    )
    assert recipe_res.status_code == status.HTTP_200_OK
    response_data = recipe_res.json()

    assert response_data["msg"] == "Success"
    assert len(response_data["body"]) == 0


def test_create_recipe():
    recipe_res = client.post(
        "/recipes/create",
        json={
            "recipeName": "Rice",
            "recipeType": "veg",
            "recipeDescription": "Plain rice",
            "recipeCuisine": "Indian",
        },
    )
    assert recipe_res.status_code == status.HTTP_201_CREATED
    response_data = recipe_res.json()

    assert response_data["msg"] == "Recipe created successfully"
    assert response_data["body"]["recipeId"] == 1


def test_get_recipes_returns_one_recipe():
    recipe_res = client.get("/recipes")
    assert recipe_res.status_code == status.HTTP_200_OK
    response_data = recipe_res.json()

    assert response_data["msg"] == "Success"
    assert len(response_data["body"]) == 1


def test_get_recipe_not_found():
    recipe_res = client.get("/recipes/0011")
    assert recipe_res.status_code == status.HTTP_404_NOT_FOUND


def test_delete_recipe():
    recipe_res = client.delete("/recipes/1")
    assert recipe_res.status_code == status.HTTP_200_OK
    response_data = recipe_res.json()

    assert response_data["msg"] == "Recipe deleted successfully"


def test_delete_recipe_not_found():
    recipe_res = client.delete("/recipes/1234")
    assert recipe_res.status_code == status.HTTP_404_NOT_FOUND
