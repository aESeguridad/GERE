#/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
from source.main import app
from source.models.client import Client


finder = Blueprint('finder',__name__)
""" Main application view module

    Routes
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    *index*  Results page
"""



@finder.route('/', methods=['GET','POST'])
def index(**kwargs):
    """.. function:: index()
    
    Returns the default page with the results of the query
    """
    #results = Client.query.filter_by(name=request.form['q']).all()
    return render_template('base.html', title='Resultados')