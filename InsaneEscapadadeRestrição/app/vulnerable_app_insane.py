import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/execute" method="POST">
            <input name="cmd" placeholder="Enter a restricted command">
            <button type="submit">Run</button>
        </form>
    '''

@app.route('/execute', methods=['POST'])
def execute():
    cmd = request.form.get('cmd', '')
    restricted_commands = ['ls', 'cat', 'echo']
    if any(rc in cmd for rc in restricted_commands):
        return "Command restricted!"
    try:
        result = os.popen(cmd).read()
        return f"<pre>{result}</pre>"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
