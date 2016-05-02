#/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request
from source.models.client import Client, ClientForm
from source.main import db

clients = Blueprint('clients',__name__)
""" Main application view module

    Routes
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    *index*  
"""

@clients.route('/', methods=['GET'])
def index(**kwargs):
    """.. function:: index()
    
    Returns the default page with the results of the query
    """
    results = Client.query.limit(20)
    return render_template('clients.html', title='Resultados', results=results)

@clients.route('/add', methods=['POST','GET'])
def AddClient():
    if request.method == 'GET':
        return render_template('AddClient.html', title=u'Añadir Cliente')
