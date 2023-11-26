#!/bin/python/

word = input('escribe una palabra: ')
chars = {}

for char in word:
    if char in chars:
        chars[char] += 1
    else:
        chars[char] = 1

for char in chars:
    count = chars[char]
    print('el caracter ', char, ' aparecio ', count, ' veces')
