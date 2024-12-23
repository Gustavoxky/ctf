import threading
from flask import Flask, request

app = Flask(__name__)
balance = 100

lock = threading.Lock()

@app.route('/')
def home():
    return f"Balance: {balance}"

@app.route('/withdraw', methods=['POST'])
def withdraw():
    global balance
    amount = int(request.form.get('amount', 0))
    if balance >= amount:
        lock.acquire()
        balance -= amount
        lock.release()
        return f"Withdrawn {amount}. New balance: {balance}"
    return "Insufficient balance!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
