# explore-python


## Topics to Cover
Python explore, will cover following topics:

- Python
- Virtual Environment
- Flask
  - Blueprints
  - Jinja templates
  - RestPlus - Swagger (todo)
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

Extend for Swagger support

```bash
echo "flask-restplus" > requirements.txt
pip install -r requirements.txt
```