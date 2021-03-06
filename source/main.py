#/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

from views.root import root
app.register_blueprint(root)

from views.clients import clients
app.register_blueprint(clients, url_prefix='/clients')