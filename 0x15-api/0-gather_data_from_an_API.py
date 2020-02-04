#!/usr/bin/python3
# get the info of a worker
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
    print("Employee {} is done with task ({}/{})"
          .format(user_json.get('name'), done_task, all_task))
    for string_title in string_task:
        print('\t {}'.format(string_title))
