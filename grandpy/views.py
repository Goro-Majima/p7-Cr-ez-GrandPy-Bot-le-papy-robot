from flask import Flask, render_template, jsonify, request
from grandpy.Main.main import process_question

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

# @app.route('/api')
# def ajax():
#     question = request.args.get('question', '')
#     response = process_question(question)
#     return jsonify(response)
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)