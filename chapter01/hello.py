from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def index():
    return "Hello World!"

@app.route("/ethan")
def hello_():
    return '<h1>Hello, ethan!</h1>'

@app.route("/<user_name>")
def hello(user_name):
    return '<h1>Hello, %s!</h1>' % user_name

if __name__ == "__main__":
    app.run()