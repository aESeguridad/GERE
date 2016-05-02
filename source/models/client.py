#/usr/bin/env python
# -*- coding: utf-8 -*-
from source.main import db
class Client(db.Model):
    __tablename__ = 'client'
    
    #: Columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    company = db.Column(db.String, nullable = True)
    vat = db.Column(db.String(11), nullable = False)
    street = db.Column(db.String, nullable = False)
    address2 = db.Column(db.String, nullable = False)
    city = db.Column(db.String, nullable = False)
    postal = db.Column(db.Integer, nullable = False)
    state = db.Column(db.String, nullable = False)
    country = db.Column(db.String, nullable = False)
    phone = db.Column(db.Integer, nullable = True)
    fax = db.Column(db.Integer, nullable = True)
    email = db.Column(db.String, nullable = True)
    web = db.Column(db.String, nullable = True)
    client_type = db.Column(db.Enum('company', 'individual'), nullable = True,
            default = 'individual')
    
    #: Relationships
    contacts = db.relationship('Contact', backref='Client', lazy='dynamic')
    
    def __init__(self, **kwargs):
        if kwargs:
            self.name = kwargs['name']
            self.company = kwargs['company']
            self.vat = kwargs['vat']
            self.street = kwargs['street']
            self.address2 = kwargs['address2']
            self.city = kwargs['city']
            self.postal = kwargs['postal']
            self.state = kwargs['state']
            self.country = kwargs['country']
            self.phone = kwargs['phone']
            self.fax = kwargs['fax']
            self.email = kwargs['email']
            self.web = kwargs['web']
            self.client_type = kwargs['client_type']
            
    def __repr__(self):
        return None


class Contact(db.Model):
    __tablename__ = 'contact'
    
    #:Columns
    id = db.Column(db.Integer, primary_key = True)
    client = db.Column(db.Integer, db.ForeignKey('client.id'), nullable = False)
    name = db.Column(db.String, nullable = False)
    street = db.Column(db.String, nullable = False)
    address2 = db.Column(db.String, nullable = False)
    city = db.Column(db.String, nullable = False)
    postal = db.Column(db.Integer, nullable = False)
    state = db.Column(db.String, nullable = False)
    country = db.Column(db.String, nullable = False)
    phone = db.Column(db.Integer, nullable = True)
    fax = db.Column(db.Integer, nullable = True)
    email = db.Column(db.String, nullable = True)
    web = db.Column(db.String, nullable = True)
    contact_type = db.Column(db.Enum('send_address', 'bill_address',
            'individual', 'worker', 'accountant', 'manager'),
            nullable = True, default = 'individual')
    
    def __init__(self, **kwargs):
        if kwargs:
            self.client = kwargs['client']
            self.name = kwargs['name']
            self.street = kwargs['street']
            self.address2 = kwargs['address2']
            self.city = kwargs['city']
            self.postal = kwargs['postal']
            self.state = kwargs['state']
            self.country = kwargs['country']
            self.phone = kwargs['phone']
            self.fax = kwargs['fax']
            self.email = kwargs['email']
            self.web = kwargs['web']
            self.contact_type = kwargs['contact_type']
            
    def __repr__(self):
        return None
        
        
        
if __name__ == "__main__":
    db.create_all()