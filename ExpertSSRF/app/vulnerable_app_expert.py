import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/fetch" method="GET">
            <input name="url" placeholder="Enter URL">
            <button type="submit">Fetch</button>
        </form>
    '''

@app.route('/fetch', methods=['GET'])
def fetch():
    url = request.args.get('url')
    if url:
        try:
            response = requests.get(url)
            return f"<pre>{response.text}</pre>"
        except Exception as e:
            return f"Error fetching URL: {e}"
    return "No URL provided!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
