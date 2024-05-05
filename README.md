# recipe

CRUD operations for recipe's

### Setting up virtual environment

It is always better to use virtual environment when working with Python tech stack.

0. Execute below command to install virtualenv dependency package

   `pip3 install virtualenv`

1. Execute below command to create virtual environment. .venv is name, you can give any name

   `python -m venv .venv`

2. Execute below command activate virtual environment.

   `source .venv/bin/activate`

### Installing dependencies

Execute `pip3 install -r requirements.txt` to install all dependenceis for this project

### Run tests

- Execute below command to run tests

  `./run_unit_tests.sh`

### PostgreSQL setup.

**Step 0**. Install docker by following [this](https://docs.docker.com/engine/install/) page

**Step 1**. Execute below docker command to run postgres server

`docker run -itd -e POSTGRES_USER=db_user_name -e POSTGRES_PASSWORD=password -p 5432:5432 -v ~/db:/var/lib/postgresql/data --name db_name postgres`

**Step 2**. Connect to postgres with specified user name and password from the step 1.

**Step 3**. Create database name(Same name should be used in `database.py` file). Current db name in database.py file is `recipe_db`.

### How to start the server

- Execute below command to start fastapi server

  `./run_app.sh`

- Execute below command to see API contract in openAPI format.

  `http://localhost:8000/docs#/`
