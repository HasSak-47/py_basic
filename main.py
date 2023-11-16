
dic = {'key': 'val', 0.2: 4, 1: 3.2}

print(dic['key'])   # 'val'
print(dic[0.2])     # 4
print(dic[1])       # 3.2

dic['p'] = 0.5
print(dic)          # {'key': 'val', 0.2: 4, 1: 3.2, 'p': 0.5}
