from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap

# Initializing application
app = Flask(__name__)