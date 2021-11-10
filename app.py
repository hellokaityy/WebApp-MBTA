"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template

from mbta_helper import find_stop_near

from flask import request


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def findLocation():
    if request.method == 'POST':
        return find_stop_near(request.form['location'])


if __name__ == '__main__':
    app.run(debug=True)

"""

"""