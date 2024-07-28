from flask import Flask, render_template, request, jsonify
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

    with open('url.txt', 'w') as file:
        file.write(text)
    

    web_scraper = ScrapeAndLLM()
    web_scraper.main()

    return 'Bill has been successfully summarized', 200

if __name__ == '__main__':
    app.run(debug=True)

