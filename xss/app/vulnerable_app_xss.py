from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return """<form action='/comment' method='POST'>
                <input name='comment' placeholder='Enter a comment'>
                <button type='submit'>Submit</button>
            </form>"""

@app.route('/comment', methods=['POST'])
def comment():
    comment = request.form.get('comment', '')
    return render_template_string(f"<h1>Your Comment:</h1><p>{comment}</p>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
