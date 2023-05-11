from flask import render_template, request, redirect
import requests
from models.char import all_chars, create_char
from services.session_info import current_user

def get_char_from_api(realm, char_name):
  api_url = f'https://us.api.blizzard.com/profile/wow/character/{realm}/{char_name}?namespace=profile-us&locale=en_US&access_token=USWAvjnlORaReA2bL8QPt1HIfnrcDGRuCA'
  response = requests.get(api_url).json()
  return response

def index():
  char = all_chars()
  return render_template('char/index.html')
# , current_user=current_user
def new():
  return render_template('char/new.html')

def create():
  char_name = request.form.get('name')
  realm = request.form.get('realm')
  create_char(id, realm, char_name)
  return redirect('/')

# def edit(id):
#   char = get_char(id)
#   return render_template('chars/edit.html', char=char)

# def update(id):
#   name = request.form.get('name')
#   image_url = request.form.get('image_url')
#   update_char(id, name, image_url)
#   return redirect('/')

# def delete(id):
#   delete_char(id)
#   return redirect('/')