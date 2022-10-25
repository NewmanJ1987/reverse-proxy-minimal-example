from flask import Flask, url_for, Response, request, Blueprint

example_blueprint = Blueprint('example_blueprint', __name__)


@example_blueprint.route("/")
def index():
    return "<pre>url_for('index', _external=True) = {}\n\n{}"\
        .format(url_for('example_blueprint.index', _external=True), request.headers)


@example_blueprint.route('/test', methods=['GET'])
def test():
    return 'See Other', 303, {'Location': url_for('example_blueprint.success')}


@example_blueprint.route('/success', methods=['GET'])
def success():
    return Response("Successfully redirected!", mimetype='text/plain'), 200