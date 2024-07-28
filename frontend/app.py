from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import sys
original_sys_path = sys.path.copy()
current_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(parent_directory)
import main
from main import ScrapeAndLLM
sys.path = original_sys_path


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_text', methods=['POST'])
def save_text():
    data = request.get_json()
    text = data.get('text')
    try: 
        with open('url.txt', 'w') as file:
            file.write(text)
        

        web_scraper = ScrapeAndLLM()
        web_scraper.main()

        return 'Bill has been successfully summarized', 200
    except Exception as e:
        return str(e), 500 

@app.route('/retrieve_text', methods=['GET'])
def retrieve_text():
    try:
        with open('llm_response.txt', 'r') as file:
            text = file.read()
        return "Bill summary: " + text, 200
    except FileNotFoundError:
        return 'No text found', 404

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('templates', filename)

if __name__ == '__main__':
    app.run(debug=True)

