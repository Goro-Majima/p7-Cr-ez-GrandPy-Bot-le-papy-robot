"""file used according to the mvt, send output to the route"""
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin

from grandpy.mainfile import process_question


app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False # keep tones when returning json file
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@app.route('/home/')
def home():
    """display homepage to the url /home/"""
    return render_template('home.html')

@app.route('/_api', methods=['POST'])
@cross_origin(origin='http://127.0.0.1:5000/_api', headers=['Content-Type', 'Authorization'])
def api_response():
    """send response to the server at url _api"""
    text = request.form['usertext']
    response = process_question(text)
    return jsonify(response)
