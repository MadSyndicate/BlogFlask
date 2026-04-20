import json

PATH_TO_DB_FILE = './easy_db.json'


def save_to_db(data):
    with open(PATH_TO_DB_FILE, 'w') as json_file:
        json.dump(data, json_file)


def get_all_blogs():
    with open(PATH_TO_DB_FILE, "r") as json_file:
        return json.load(json_file)


def post_blog(post):
    current_collection = get_all_blogs()
    current_max_id_post = max(current_collection, key=lambda x: x['id'])
    new_post_id = current_max_id_post['id'] + 1
    post['id'] = new_post_id
    current_collection.append(post)
    save_to_db(current_collection)
    return new_post_id


def delete_post(post_id):
    current_collection = get_all_blogs()
    new_collection = [p for p in current_collection if p.get('id') != post_id]
    save_to_db(new_collection)
