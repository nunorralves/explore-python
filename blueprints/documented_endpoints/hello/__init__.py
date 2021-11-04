from flask import request
from flask_restplus import Namespace, Resource, fields

namespace = Namespace('hello', 'Hello World related endpoints')

hello_model = namespace.model('Hello', {
    'message': fields.String(
        readonly=True,
        description='Hello world message'
    )
})

hello_example = {'message': 'Hello World!'}

@namespace.route('')
class HelloWorld(Resource):

    @namespace.marshal_list_with(hello_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        '''Hello message endpoint'''

        return hello_example