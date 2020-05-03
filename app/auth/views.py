from flask import render_template,redirect,url_for, flash,request
from . import auth
from flask_login import login_user,logout_user,login_required,current_user
from ..models import User,Pitch
from .forms import LoginForm,SignUpFrom
