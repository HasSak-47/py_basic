#!/bin/python/

# para guardar todas las letras que se van a buscar como llave
# y los valores seran la cantidad de veces que aparecieron
chars = {}
words = []

chars_total = int(input('numero total de letras: '))
words_total = int(input('numero total de palabras: '))

for i in range(chars_total):
    # se crea el par char con el valor 0
    # 0 debido a que esta char aun no se a encotrado
    chars[input('letra: ')] = 0

for i in range(words_total):
    words.append(input('palabra: '))

for word in words:
    print('checando palabra: ', word)
    # checa cada char de diccionario
    for char in chars:
        # si la char esta en la word añade uno a la cuenta
        if char in word:
            chars[char] += 1

print('total de letrass encontradas')
for char in chars:
    total = chars[char]
    print('la letra ', char, ' aparecio ', total, ' veces')
