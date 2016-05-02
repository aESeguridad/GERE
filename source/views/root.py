#/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
from source.main import app


root = Blueprint('root',__name__)
""" Main application view module

    Routes
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    *index*  Index page
"""


@root.route('/', methods=['GET'])
def index():
    """.. function:: index()
    
    Returns the default page
    """
    return render_template('base.html', title='Inicio')