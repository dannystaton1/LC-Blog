from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2
from flask_sqlalchemy import SQLALchemy


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config["DEBUG"] = True

