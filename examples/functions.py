#!/bin/python/

def pretty_print(dic):
    for k in dic:
        v = dic[k]
        print(k, ': ', v)


def input_type():
    typ = input('type: ')
    inpt = input('value: ')
    if typ == 'int':
        return int(inpt)
    elif typ == 'float':
        return float(inpt)
    return inpt


total = int(input('total: '))
dic = {}
for i in range(total):
    key = input('key: ')
    val = input_type()
    dic[key] = val

pretty_print(dic)
