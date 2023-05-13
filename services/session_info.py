from flask import session
from models.users import find_user_by_user_name

def current_user():
  # if a user is logged in:
  if session.get('user_id'):
    return find_user_by_user_name(session['user_id'])
  else:
    return None