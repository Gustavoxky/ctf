from flask import Flask, request, jsonify
import jwt
import datetime

SECRET_KEY = "supersecret"

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/login" method="POST">
            <input name="username" placeholder="Username">
            <button type="submit">Login</button>
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    if username:
        token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)}, SECRET_KEY, algorithm="HS256")
        return jsonify({'token': token})
    return "Missing username!", 400

@app.route('/admin')
def admin():
    token = request.headers.get('Authorization')
    if not token:
        return "Token missing!", 403
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if decoded['user'] == 'admin':
            return "Welcome admin! FLAG{jwt_token_tampered}"
        return "Unauthorized!", 403
    except jwt.ExpiredSignatureError:
        return "Token expired!", 403
    except jwt.InvalidTokenError:
        return "Invalid token!", 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
