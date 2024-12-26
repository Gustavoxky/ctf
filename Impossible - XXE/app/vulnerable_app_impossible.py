from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        xml_data = request.data
        try:
            tree = ET.fromstring(xml_data)
            flag = tree.find('flag').text
            return f"Extracted Flag: {flag}"
        except Exception as e:
            return f"Error: {e}"
    return '''
        <form method="POST" enctype="text/plain">
            <textarea name="xml" rows="10" cols="30">
                <flag>Enter your XML here</flag>
            </textarea>
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
