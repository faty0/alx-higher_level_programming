#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    zer = [0, 0]
    if len(a) == 0:
        a.extend(zer)
    if len(a) == 1:
        a.append(0)
    if len(b) == 0:
        b.extend(zer)
    if len(b) == 1:
        b.append(0)
    return (a[0] + b[0], a[1] + b[1])
