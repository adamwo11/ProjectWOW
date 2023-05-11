from flask import render_template, request, redirect
from models.users import create_user

def new():
  return render_template('users/new.html')

def create():

  email = request.form.get('email')
  password = request.form.get('password')
  create_user(email, password)
  return redirect('/')