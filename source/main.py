from flask import Flask, render_template

app = Flask(__name__)

from views.root import root
app.register_blueprint(root)
