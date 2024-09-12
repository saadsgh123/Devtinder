from flask import Flask
from main import app
app.secret_key = 'your_super_secret_key'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
