from fastapi import FastAPI
from api import recipe_apis
from database import Base, engine


def start_app():

    fastapi_app = FastAPI(
        title="Recipe",
        description="Recipe API Services",
        summary="Recipe api services",
        version="0.0.1",
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
        contact={
            "name": "Rishabh Kumar",
            "email": "rishabh.kumar94@outlook.com",
        },
    )
    return fastapi_app


Base.metadata.create_all(bind=engine)

app = start_app()


app.include_router(recipe_apis.router)
