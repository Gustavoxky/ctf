import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Try to list the files in this directory by accessing /execute?cmd=<your_command>"

@app.route('/execute', methods=['GET'])
def execute():
    cmd = request.args.get('cmd', '')
    result = os.popen(cmd).read()
    return f"<pre>{result}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
