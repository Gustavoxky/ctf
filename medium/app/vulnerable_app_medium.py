import sqlite3
from flask import Flask, request

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'supersecret')")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "Access /login?username=<name> to find the flag."

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username', '')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}'"
    print("Executing query:", query)
    c.execute(query)
    result = c.fetchone()
    conn.close()
    if result:
        return "Welcome, admin! Here is your flag: FLAG{sql_injection_victory}"
    return "Invalid user."

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=80)
