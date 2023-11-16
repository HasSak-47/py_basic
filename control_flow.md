# If 
El if ejecuta todo lo que esta dentro de este si y solo si la condicion es evaluada como verdadera.
```python
if 0 == 1:
    print('0 es igual a 1')
```
en este caso el `print('0 es igual a 1')` nunca ocurrira ya que `0 == 1` es `False`

# if else
En caso de un if else el codigo dentro del else se ejecutara si la evaluacion de la condicion anterior es `False`

```python
if 0 == 1:
    print('0 es igual a 1')
else:
    print('0 no es igual a 1')
```

# elif
El elif es equivalente a tener un if dentro de un else, se pueden colocar tantos como quieras

```python
if x == 0:
    print('x es igual a 0')
elif x == 1:
    print('x es igual a 1')
elif x == 2:
    print('x es igual a 2')
else:
    print('x no es igual a 0, 1 o 2')
```


# While loop
el while loop ejecuta todo lo que esta dentro de este hasta que la condicion sea evaluada como falsa
```python
x = 0
while x < 10:
    print(x)
    x += 1
```

## Salida temprana
Se puede salir temprano de un while utilizando la keyword `break`
```python
x = 0
while x < 10:
    if x == 4:
        break
    print(x)
    x += 1
```
en este ejemplo el programa se sale del while cuando `x == 4`

## Saltar codigo
Se puede saltar codigo dentro de un while utilizando la keyword `continue`
```python
arr = [0, 1, 2, 3, 4, 5]
while x < 10:
    if x % 2 == 0:
        continue
    print(x)
```
en este ejemplo el programa no ejecuta el `print(x)` cuando `x % 2 == 0` es decir cuando x es par
