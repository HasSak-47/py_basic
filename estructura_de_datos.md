# Estructura de datos
Las estructuras de datos son una forma de tener varios elementos, estos elementos pueden ser cualquier cosa, dentro de una sola variable, a la cual se puede acceder a estos elementos de diferente forma.

Cuando una variable es añadida a una estructura, en el caso de los primitivos esta es copiada, en casos de estructuras es una 'referencia', es decir que si por ejemplo tienes una estructura A, y la pones dentro de estructura B, si modificas la estructura A, también se modificará la estructura dentro de B

```python
A = [1, 2 ,3]
B = [A]
A[0] = 0
print(A)        # [0, 2, 3]
print(B)        # [[0, 2, 3]]
```

Las estructuras de datos tienen forma de acceder a los elementos dentro de esta especificados por su tipo, y ademas pueden tener extras operaciones, como añadir, quitar, substituir elementos etc.

## Listas
Una lista en python es un conjunto ordenado de elementos, a las listas se les puede agregar elementos al final con el metodo `.append(val)`
y obtener y remover el ultimo elemento con `.pop()`
Una lista se declara asi:
```python
x = []                  # lista vacia
x = [0, 3, 'str']       # lista con puros elementos
y = 1
x = [y, 3, 'str']       # lista con con variables

x.append(10)            # añadir 10 a la lista
y = x.pop()             # remover el ultimo elemento y guardarlo en y
```

Para acceder a un elemento dentro de una lista se utiliza la syntaxis `lista[indice]`, donde el indice es un numero entero el cual especifica el indice del elemento, el indice inicia en 0. Si pones un indice igual o mas grande que el numero de elementos dentro de la lista python crashea

```python
x = [0, 3, 'str']
print(x[0])     # 0
print(x[1])     # 3
print(x[2])     # str
```

para sublistas se hace de la misma forma
```python
x = [0, [2, 4], 'str']
print(x[0])         # 0
print(x[1][0])      # 2
print(x[1][1])      # 4
print(x[2])         # str
```

### String
las strings son un tipo especial de lista, la cual contiene solamente caracteres, las mismas operaciones que se le puede hacer a una lista se le pueden hacer a una str pero no en viceversa.

## Tuplas
Una tupla en python es similar a una lista, solo que los elementos dentro de esta son inmutables, y no puede crecer ni decrecer
```python
x = (0, 3, 'str')
print(x(0))     # 0
print(x(1))     # 3
print(x(2))     # str
```

## Diccionarios
Un diccionario es un conjunto de pares llave, elemento. al cual se le puede añadir mas pares llave elemento, siempre y cuando la llave sea un elemento 'hasheable', para poder añadir un par a una lista se hace de la forma `dic[key] = val`

```python
x = {0: 'str', 'key': 'val', 2.: 0}
print(x[0])         # str
print(x['key'])     # val
print(x[2.])        # 0

x['new'] = 'test'   # añadio par (new, test) al diccionario
```




