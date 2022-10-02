from tinydb import TinyDB, Query
from tinydb.operations import add
from helpers.helpers import remove_duplicates

db = TinyDB('db.json')


def create_user(user_id):
    if not get_user(user_id):
        db.insert({'user_id': user_id, 'presets': []})


def get_user(user_id):
    User = Query()
    return db.search(User.user_id == user_id)


def add_preset(user_id, preset):
    User = Query()


    get_current = get_presets(user_id)
    get_current.append(preset)

    remove_duplicate_entries = remove_duplicates(get_current)

    db.update({'presets': remove_duplicate_entries}, User.user_id == user_id)
    


    # db.update(add('presets', new_preset), User.user_id == user_id)




def get_presets(user_id):
    User = Query()
    return db.search(User.user_id == user_id)[0]['presets']


def delete_preset(user_id, preset):
    User = Query()
    presets = get_presets(user_id)
    
    remove = [p for p in presets if p != preset]


    db.update({'presets': remove}, User.user_id == user_id)


def delete_all_presets(user_id):
    User = Query()
    db.update({'presets': []}, User.user_id == user_id)
