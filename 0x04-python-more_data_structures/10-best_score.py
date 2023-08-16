#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    listt = list(a_dictionary)
    first_value = a_dictionary[listt[0]]
    best_key = listt[0]
    for k, v in a_dictionary.items():
        if v > first_value:
            first_value = v
            best_key = k
    return best_key
