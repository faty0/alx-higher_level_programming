#!/usr/bin/python3
''' script that adds all arguments to a Python list,
and then save them to a file
'''


from sys import argv


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_list = []
if len(argv) > 1:
    try:
        my_list = load_from_json_file("add_item.json")
    except Exception as e:
        with open("add_item.json", 'w', encoding="utf_8")
    for arg in argv:
        my_list.append(arg)
    save_to_json_file(my_list, "add_item.json")

