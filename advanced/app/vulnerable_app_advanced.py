from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Access /download?file=<filename> to exploit the vulnerability."

@app.route('/download', methods=['GET'])
def download():
    file = request.args.get('file', '')
    path = os.path.join('/app', file)
    try:
        return send_file(path)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
