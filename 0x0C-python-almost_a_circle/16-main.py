#!/usr/bin/python3
""" 16-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
    jli = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(jli)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(jli), jli))
    print("[{}] {}".format(type(list_output), list_output))
