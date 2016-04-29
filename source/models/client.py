#/usr/bin/env python
# -*- coding: utf-8 -*-

from source.main import db

class Client(db.Model):
    __tablename__ = 'client'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    company = db.Column(db.String, nullable = True)
    vat = db.Column(db.String(11), nullable = False)
    
    def __init__(self, **kwargs):
        pass
    def __repr__(self):
        pass
    def getcontacts(self):
        pass