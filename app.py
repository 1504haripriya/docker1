from flask import Flask

app = Flask(__name__)


@app.route('/<food>')
def restaurants(food):
    return " Hello biriyani"


if __name__ == '__main__':
    app.run( )
