from flask import render_template, request, redirect, session
from models.users import find_user_by_user_name
import bcrypt

def new():
  return render_template('sessions/new.html')

def create():
  user_name = request.form.get('user_name')
  password = request.form.get('password')
  user = find_user_by_user_name(user_name)
  if user == None:
    return redirect('/sessions/new')
  
  valid_password = bcrypt.checkpw(password.encode(), user['password_digest'].encode())
  if valid_password:
    session['user_id'] = user['id'] # logs the user in
    return redirect('/')
  else:
    return redirect('/sessions/new')

def delete():
  session.clear() # logs the user out
  return redirect('/')