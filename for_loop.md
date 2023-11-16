# For loop
El for loop se utiliza para iterar atraves de un iterador.

## iterador range()
El `range(x)` itera a traves del 0 a uno menos que x.
```python
for i in range(10):
    print(i)
```

## Iterar lista
```python
l = [0, 1 ,2]
for i in l:
    print(i)
```
imprime toda la lista

## Iterar tupla
```python
t = (0, 1 ,2)
for i in t:
    print(i)
```
imprime toda la tupla

## Iterar diccionario
Cuando se itera atraves de un diccionario, se esta iterando por todas las llaves del diccionario
```python
dic = {
    'key0': 'val0',
    'key1': 'val1',
    'key2': 'val2',
    'key3': 'val3',
}
for k in dic:
    print(k)
```
imprime todas las llaves

para acceder al par llave valor se puede hacer de la siguiente forma
```python
dic = {
    'key0': 'val0',
    'key1': 'val1',
    'key2': 'val2',
    'key3': 'val3',
}
for k, v in dic.items():
    print(k, v)
```
imprime todos los valores llave, valor


dentro de un for loop se puede usar `continue` y `break`
