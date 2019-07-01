from flask import Flask, render_template, jsonify, request
from grandpy.mainfile import process_question

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # to keep tones when returning json file

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/api')
def ajax():
    question = request.args.get('question', '')
    response = process_question('grand py dirige moi vers la gare de montparnasse')
    return jsonify(response)
    
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)