from flask import Flask
from main import app

# the run file to start the program
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
