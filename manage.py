
test = [
        'uno',
        'dos',
        'tres',
        'cuatro',
        'cinco',
        'seis',
        'siete',
        'ocho',
        'nueve',
        'diez',
        ]

dic = {}
for t in test:
    print(f'escriba algo: {t}')
    l = len(t)
    if not l in dic:
        dic[l] = [t]
    else:
        dic[l].append(t)

print(dic)


x = int(input('...'))
while x < 0 and x > 10:
    x = int(input('...'))
