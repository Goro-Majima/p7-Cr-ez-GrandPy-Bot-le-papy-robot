from flask import Flask, render_template, jsonify, request
from grandpy.mainfile import process_question
from grandpy.classes import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # keep tones when returning json file

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

# @app.route('/_api', methods= ['GET','POST'])
# def api_response():
# 	if request.method == 'POST':
# 		text = request.form['usertext']
# 		response = process_question(text)
# 		# return render_template('momo.html',text=response)
# 		return jsonify(response)

@app.route('/_api/', methods= ['GET','POST'])
def api_response():
<<<<<<< HEAD
    text = request.args.get('usertext','disney village')
=======
    text = request.args.get('usertext','abcd')
    print(text)
>>>>>>> 371fd12dab5d5f837fc1531d942b313924e3eecd
    response = process_question(text)
    return jsonify(response)
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)