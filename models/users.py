from db.db import sql
import bcrypt

def create_user(email, password):
  password_digest = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
  sql('INSERT INTO users(email, password_digest) VALUES(%s, %s) RETURNING *', [email, password_digest])

def find_user_by_email(email):
  users = sql('SELECT * FROM users WHEREemail = %s', [email])
  # if one or more users is found:
  if len(users) > 0:
    return users[0] # return the first user.
  else:
    return None

def find_user_by_id(id):
  users = sql('SELECT * FROM users WHERE id = %s', [id])
  return users[0]