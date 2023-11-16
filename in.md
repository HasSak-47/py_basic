# Keyword in
La keyword in tiene dos funciones como operador y como elemento dentro de un for loop

## Operador in 
el operador in checa si un valor esta dentro de una estructura de datos, en el caso de la lista y la tupla, funciona de manera simple, `a in c` regresa `True` si a esta en c, `false` si no lo esta. en el caso del diccionario regresa `True` si existe una llave con el mismo valor que `a`sin importar que exista este valor en los valores del diccionario.

```python
x = [0, 1, 2, 3]
y = int(input('input: '))
if y in x:
    print('y esta en x')
else:
    print('y no esta en x')

# elimniar los espacios 2 o mas de una cadena
string = 'string   con   mucho     espacios'
while '  ' in string:                       # replaza '  ' con ' ' hasta que no queden '  '
    string = string.replace('  ', ' ')
```

replace es un metodo especial de las cadenas que remplaza la primera instancia de la primera cadena con la segunda

## Keyword In
Esta sirve para separar el for en 2 partes, la parte de la variable y la parte del iterador.
```python
for var in iter:
    pass
```

Un iterador es una cosa que itera a traves de un conjunto de valores. por ejemplo
```python
for x in [0, 1, 2, 3]:
    print(x)
```
imprime
```
0
1
2
3
```
la lista es convertida en un iterador, y luego pasa por un valor lo asigna a x, luego pasa por el siguiente valor hasta que ya no haya mas valores
