from flask import Blueprint, request, render_template

jinja_endpoints = Blueprint('jinja_template', __name__, url_prefix='/jinja_template')

@jinja_endpoints.route('')
def get_template():
    top = request.args.get('top') if 'top' in request.args else ''
    bottom = request.args.get('bottom') if 'bottom' in request.args else ''

    return render_template('template.html', top=top, bottom=bottom)