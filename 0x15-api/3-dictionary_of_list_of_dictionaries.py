#!/usr/bin/python3
# get the info of a worker
from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    user_name = get("https://jsonplaceholder.typicode.com/users/{}"
                    .format(argv[1]))
    todo_user = get("https://jsonplaceholder.typicode.com/todos?userId={}"
                    .format(argv[1]))
    user_json = user_name.json()
    list_json = todo_user.json()
    all_task = 0
    done_task = 0
    string_task = []

    for dict_data in list_json:
        if dict_data.get('completed'):
            done_task += 1
            string_task.append(dict_data.get('title'))
        all_task += 1

    with open('{}.json'.format(int(argv[1])), 'w') as read_file:
        json_list = []
        for dicts in list_json:
            json_list.append({'task': dicts.get('title'),
                              'completed': dicts.get('completed'),
                              'username': user_json.get('name')})
            dict_jsons = {argv[1]: json_list}
            dump(dict_jsons, read_file)
