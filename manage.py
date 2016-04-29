#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_script import Manager
from source.main import app


app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'ea746a854f204c42bf8683523808f326'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://source/database.sqlite3'
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
