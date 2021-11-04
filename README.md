# explore-python


## Topics to Cover
Python explore, will cover following topics:

- Python
- Virtual Environment
- Flask
  - Blueprints
  - Jinja templates
  - RestPlus - Swagger
- Poetry (todo)

<br/>

## Steps to configure
With Python installed, lets setup virtual environment and activate it:

```
sudo apt install python3.9-venv
python3 -m venv .venv
source ./venv/bin/activate

deactivate
```

Now, let's install Flask. We can install directly:


```
pip install Flask
```

or through requirements.txt file


```bash
echo "flask" > requirements.txt
pip install -r requirements.txt
```

Create main.py file

```
export FLASK_APP=main.py
export FLASK_ENV=development
flask run
```

## Extend for Swagger support

```bash
echo "flask-restplus" > requirements.txt
echo "Werkzeug==0.16.1" > requirements.txt
pip install -r requirements.txt
```

## Replace PIP by Poetry

- Install `poetry` using curl

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

- Start using it on an existing project

```bash
poetry init
```

Following interactive prompts, we get a new ```pyproject.toml``` file

- Set environment

```
export FLASK_APP=main.py
export FLASK_ENV=development
```

- Run with poetry (built-in virtual environment)

```bash
poetry install
poetry run flask run
```
