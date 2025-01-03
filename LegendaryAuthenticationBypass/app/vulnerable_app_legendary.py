from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/login" method="POST">
            <input name="username" placeholder="Username">
            <input name="password" placeholder="Password" type="password">
            <button type="submit">Login</button>
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "admin" and password == "supersecret":
        resp = make_response("Welcome, admin! Here is your flag: FLAG{legendary_auth_bypass}")
        resp.set_cookie('auth', 'admin')
        return resp
    return "Invalid credentials!"

@app.route('/admin')
def admin():
    auth = request.cookies.get('auth')
    if auth == "admin":
        return "Welcome to the admin panel! FLAG{legendary_auth_bypass}"
    return "Unauthorized!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
