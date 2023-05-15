from db.db import sql

def all_chars():
  return sql('SELECT * FROM char ORDER BY id')

def get_char(id):
  char = sql("SELECT * FROM char WHERE id = %s", [id])
  return char[0]

def create_char(name, realm, level, img_url, gender, classes, race, faction):
  sql('INSERT INTO char(name, realm) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *', [name, realm, level, img_url, gender, classes, race, faction])

def update_char(id, name, realm, level, img_url, gender, classes, race, faction):
  print('woof')
  sql('UPDATE char SET name=%s, realm=%s, level=%s, img_url=%s, gender=%s, classes=%s, race=%s, faction=%s WHERE id=%s RETURNING *', [name, realm, level, img_url, gender, classes, race, faction, id])
print('woof')
def delete_char(id):
  sql('DELETE FROM char WHERE id=%s RETURNING *', [id])

def like_char(char_id, user_id):
  sql("INSERT INTO likes(user_id, char_id) VALUES(%s, %s) RETURNING *", [user_id, char_id])