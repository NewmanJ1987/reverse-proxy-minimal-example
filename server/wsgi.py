from flask import Flask, url_for, Response, request
from example_blueprint import example_blueprint
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.register_blueprint(example_blueprint)

def run_proxy():
    return ProxyFix(app, x_for=1, x_host=1, x_port=1, x_proto=1, x_prefix=1)
    