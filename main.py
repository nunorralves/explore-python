from flask import Flask, request
from blueprints.basic_endpoints import basic_endpoints
from blueprints.jinja_endpoints import jinja_endpoints
from blueprints.documented_endpoints import blueprint as documented_endpoints


app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

app.register_blueprint(basic_endpoints)
app.register_blueprint(jinja_endpoints)
app.register_blueprint(documented_endpoints)


if __name__ == "__main__":
  app.run()