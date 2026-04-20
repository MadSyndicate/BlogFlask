import json

PATH_TO_DB_FILE = './easy_db.json'

def get_all_blogs():
    with open(PATH_TO_DB_FILE, "r") as json_file:
        return json.load(json_file)
