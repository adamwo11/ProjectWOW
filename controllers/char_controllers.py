from flask import render_template, request, redirect, session
import requests
from models.char import all_chars, get_char, create_char, update_char, delete_char, like_char
from services.session_info import current_user

def get_char_from_api(realm, char_name):
  api_url = f'https://us.api.blizzard.com/profile/wow/character/{realm}/{char_name}?namespace=profile-us&locale=en_US&access_token=USWAvjnlORaReA2bL8QPt1HIfnrcDGRuCA'
  response = requests.get(api_url).json()
  return response

def index():
  chars = all_chars()
  return render_template('chars/index.html', chars=chars, current_user=current_user())

def new():
  return render_template('chars/generate.html')

def create():
  char_name = request.form.get('name')
  realm = request.form.get('realm')
  create_char(char_name, realm)
  return redirect('/')

def edit(id):
  char = get_char(id)
  return render_template('chars/edit.html', char=char)

def update(id):
  name = request.form.get('name')
  realm= request.form.get('realm')
  level= request.form.get('level')
  img_url = request.form.get('img_url')
  gender= request.form.get('gender')
  classes= request.form.get('class')
  race= request.form.get('race')
  faction= request.form.get('faction')
  update_char(id, name, realm, level, img_url, gender, classes, race, faction)
  return redirect('/')

def delete(id):
  delete_char(id)
  return redirect('/')

def like(id):
  like_char(id, session['user_id'])
  return redirect('/')