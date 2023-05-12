from db.db import sql

def all_chars():
  return sql('SELECT * FROM char ORDER BY id')

def get_char(id):
  char = sql("SELECT * FROM char WHERE id = %s", [id])
  return char[0]

def create_char(char_name, realm, level, gender, classes, race, faction):
  sql('INSERT INTO char(char_name, realm) VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING *', [char_name, realm, level, gender, classes, race, faction])