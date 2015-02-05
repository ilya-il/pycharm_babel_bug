__author__ = 'ilya_il'

from flask import Flask, render_template
from flask.ext.babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def hello_world():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
