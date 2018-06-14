import numpy as np
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/fish-classification', methods=['POST'])
def classification():
    #ダミーデータ返却
    result = [
        {   'name' : 'haze',
            'confidence' : '0.98828125'
        },
        {   'name' : 'kasago',
            'confidence' : '0.0012414'
        },
        {   'name' : 'kisu',
            'confidence' : '0.0000414'
        }
    ]
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()