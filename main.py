"""
Uruban Coders Guild - Black Wallstreet Student Projects
ENTRY POINT
"""
from flask import Flask, jsonify, render_template, url_for
from flask_cors import (CORS, cross_origin)
from os import environ
from uuid import uuid4



app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
if "FLASK_SECRET_KEY" in environ:
    app.secret_key = environ["FLASK_SECRET_KEY"]
else:
    environ["FLASK_SECRET_KEY"] = str(uuid4())
CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template('index.html')

@app.route('/thank_you', methods=['GET'], strict_slashes=False)
def thank_you():
    return render_template('index.html')

@app.route('/donate', methods=['GET'], strict_slashes=False)
def donate():
    return render_template('index.html')

@app.route('/red_wing_cafe', methods=['GET'], strict_slashes=False)
def red_wing_cafe():
    return render_template('projects/red_wing_cafe.html')


"""
ERROR HANDLERS
"""

@app.errorhandler(400)
def bad_request(error) -> str:
    """
    Request is bad
    """
    return jsonify({"error": "Bad Request, https required"}), 400


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(403)
def Forbidden(error) -> str:
    """
    Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(401)
def Unauthorized(error) -> str:
    """
    Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
