#/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
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
    client_type = db.Column(db.Enum('company', 'individual',name='enum_client_type'), nullable = True,
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

class ClientForm(Form):
    client_type = SelectField('Tipo', choices=[('company',u'Empresa'),('individual','Particular')])
    name = StringField(u'Nombre', validators=[DataRequired(message='Debes introducir un nombre')])
    company = StringField(u'Compañía', validators=None)
    vat = StringField(u'CIF/NIF', validators=[DataRequired()])
    street = StringField(u'Dirección', validators=[DataRequired()])
    address2 = StringField(u'Dirección', validators=None)
    city = StringField(u'Población', validators=[DataRequired()])
    postal = StringField(u'Cód. Postal', validators=[DataRequired()])
    state = StringField(u'Provincia', validators=[DataRequired()])
    country = StringField(u'País', validators=[DataRequired()], default=u'España')
    phone = StringField(u'Telf.', validators=[DataRequired()])
    fax = StringField(u'Fax', validators=None)
    email = StringField(u'E-mail', validators=None)
    web = StringField(u'Web', validators=None)

class Contact(db.Model):
    """
    Contacto adicional
    """
    __tablename__ = 'contact'
    #:Columns
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    name = db.Column(db.String, nullable=False)
    street = db.Column(db.String, nullable=False)
    address2 = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    postal = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=True)
    fax = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String, nullable=True)
    web = db.Column(db.String, nullable=True)
    contact_type = db.Column(db.Enum('send_address', 'bill_address',
                                     'individual', 'worker', 'accountant',
                                     'manager', name='enum_contact_type'),
                             nullable=True, default='individual')
    
>>>>>>> refs/remotes/origin/master
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
