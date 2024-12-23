import pickle
from flask import Flask, request

app = Flask(__name__)

def deserialize(data):
    return pickle.loads(data)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            data = request.data
            obj = deserialize(data)
            return f"Deserialized object: {obj}"
        except Exception as e:
            return f"Error: {str(e)}"
    return "Send a POST request with serialized data to see what happens."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
