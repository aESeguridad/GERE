#/usr/bin/env python
# -*- coding: utf-8 -*-
from source.main import db

class Client(db.Model):
    __tablename__ = 'client'
    
    #: Column
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    company = db.Column(db.String, nullable = True)
    vat = db.Column(db.String(11), nullable = False)
    
    #: Relationship
    contacts = db.relationship('Contact', backref='Client', lazy='dynamic')
    
    def __init__(self, **kwargs):
        if kwargs:
            self.name = kwargs['name']
    def __repr__(self):
        pass