"""file used according to the mvt, send output to the route"""
from flask import Flask, render_template, jsonify, request
from grandpy.mainfile import process_question


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # keep tones when returning json file

@app.route('/')
@app.route('/home/')
def home():
    """display homepage to the url /home/"""
    return render_template('home.html')

# @app.route('/_api', methods=['POST'])
# def api_response():
#     """send response to the server at url _api"""
#     # text = request.form['usertext_field']
#     text = 'tu peux me trouver saint gilles a lile de la reunion'
#     response = process_question(text)
#         # return render_template('momo.html',text=response)
#     return jsonify(response)

@app.route('/_api/', methods= ['GET'])
def api_response():
    text = request.args.get('usertext_field')
    print(text)
    print(6)
    response = process_question(text)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
