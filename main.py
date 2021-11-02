from flask import Flask, request
from blueprints.basic_endpoints import basic_endpoints
from blueprints.jinja_endpoints import jinja_endpoints

app = Flask(__name__)
app.register_blueprint(basic_endpoints)
app.register_blueprint(jinja_endpoints)

if __name__ == "__main__":
  app.run()