from flask import Flask, render_template
from flask.ext.babel import Babel


app = Flask(__name__)
app.config.from_object("bee3.config")
babel = Babel(app)


@app.route('/')
def index():
    return render_template("frontend/index.html")


