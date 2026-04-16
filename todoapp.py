from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Show a simple test page first
    return 'Hello World!'

if __name__ == '__main__':
    # Run the Flask app
    app.run()
