from flask import render_template, request, redirect
from models.users import create_user

def new():
  return render_template('users/new.html')

def create():
  user_name = request.form.get('user_name')
  password = request.form.get('password')
  create_user(user_name, password)
  return redirect('/')