from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_text', methods=['POST'])
def save_text():
    data = request.get_json()
    text = data.get('text')

    with open('url.txt', 'w') as file:
        file.write(text)

    return 'Text saved successfully', 200

if __name__ == '__main__':
    app.run(debug=True)

