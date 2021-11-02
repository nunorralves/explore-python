from flask import Blueprint, request

# name (str) – The name of the blueprint. 
#   Will be prepended to each endpoint name
#import_name (str) – The name of the blueprint package, usually __name__. 
#   This helps locate the root_path for the blueprint.
# url_prefix (Optional[str]) – A path to prepend to all of the blueprint’s 
#   URLs, to make them distinct from the rest of the app’s routes.
basic_endpoints = Blueprint('api', __name__, url_prefix='/basic_api')

@basic_endpoints.route('/hello')
def hello_world():
    return {'message': 'Hello World!'}

@basic_endpoints.route('/entities', methods=['GET', 'POST'])
def entities():
    if request.method == "GET":
        return {
            'message': 'This endpoint should return a list of entities',
            'method': request.method
        }
    if request.method == "POST":
        return {
            'message': 'This endpoint should create an entity',
            'method': request.method,
            'body': request.json
        }

@basic_endpoints.route('/entities/<int:entity_id>', methods=['GET', 'PUT', 'DELETE'])
def entity(entity_id):
    if request.method == "GET":
        return {
            'id': entity_id,
            'message': 'This endpoint should return the entity {} details'.format(entity_id),
            'method': request.method
        }
    if request.method == "PUT":
        return {
            'id': entity_id,
            'message': 'This endpoint should update the entity {}'.format(entity_id),
            'method': request.method,
            'body': request.json
        }
    if request.method == "DELETE":
        return {
            'id': entity_id,
            'message': 'This endpoint should delete the entity {}'.format(entity_id),
            'method': request.method
        }