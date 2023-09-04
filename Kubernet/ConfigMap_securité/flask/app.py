from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    key1 = os.environ.get('KEY1', 'default_value')
    password = os.environ.get('PASSWORD', 'default_password')
    print("THIS IS A TEST")
    return f'KEY1: {key1}, PASSWORD: {password}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
