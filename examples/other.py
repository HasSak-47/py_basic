#!/bin/python/

len = int(input('lenght: '))
arr = []
for i in range(len):
    arr.append(input('word: '))

# muestra cada segunda palabra
for i in range(0, len, 2):
    print(arr[i])

# muestra cada tercera palabra
for i in range(0, len, 2):
    print(arr[i])

n = int(input('n: '))
# muestra cada n palabra
for i in range(0, len, n):
    print(arr[i])
