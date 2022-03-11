from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os 

db = SQLAlchemy()   

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
