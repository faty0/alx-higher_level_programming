#!/usr/bin/python3
''' script that adds all argv to a Python list,
and then save them to a file
'''


from sys import argv


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []
for i in range(1, len(argv)):
    my_list.append(argv[i])
save_to_json_file(my_list, "add_item.json")
