from flask import Flask
# from config import Config
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# bootstrap = Bootstrap

# Initializing application
app = Flask(__name__)


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):


    # Initializing Flask Extensions
    

    login_manager.init_app(app)