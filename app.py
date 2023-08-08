from flask import Flask, jsonify, request,render_template, send_from_directory
from util import predict,loaded_pipe
import requests

url = 'http://localhost:5000/predict'
data = {'text': 'I love this chat bot!'}

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        text = [input_text]
        predictions = predict(loaded_pipe, text)
        return render_template('index.html', predictions=predictions, input_text=input_text)
    return render_template('index.html')

@app.route('/style.css')
def style():
    return send_from_directory(app.root_path, 'style.css')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)