#/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
from source.main import app
from source.models.client import Client


clients = Blueprint('finder',__name__)
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