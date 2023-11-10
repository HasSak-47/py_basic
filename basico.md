# Comentarios
Son parte del codigo las cuales no hacen nada python las elimina cuando corre el programa solo ayudan al lector saber que esta haciendo el codigo
También sirven para eliminar partes del codigo sin borrarlas del archivo
```python
x = 1 + 2   # suma 1 + 2 y lo guarda en x
# multiplica 2 * 2 y lo guarda en x
x = 2 * 2
```

# Variables
Las variables son secciones de memoria con un nombre y tipo, donde se guarda un valor,
por ejemplo puedo crear la variable de nombre `x` de tipo `int` con un valor `1`

Una variable puede tener cualquier nombre siempre y cuando inicie con una letra, y este compuesto de letras, \_, y números.

## Creación
Python es un lenguaje de tipos dinámicos es decir que una variable puede tener varios tipos durante su vida
puede iniciar como `int` y luego ser convertido otro tipo como `str`

```python
x = 1       # Se creo x tipo 'int' que vale 1
x = 2       # ahora x vale 2
x = "test"  # Ahora x es una str que vale 'test'
```
### Pista de tipo
Es una parte de la creacion de la variable que ayuda a saber que tipo es
lo unico que hace es darle una idea al programador de que tipo es 
en realidad no hace nada, es pura decoracion
```python
x : int = 1 # Se creo x tipo 'int' que vale 1
```

## Creación y asignación
### Números enteros
Son todos los números enteros con infinita precisión
```python
x = 0
y : int = 0  
```

### Números decimales/números reales
Es un tipo de número el cual representa un número decimal
estos no tienen una gran precisión pero normalmente no importa
```python
x = 0.
y : float = 0.
```
### Booleanos
Es una variable que solo tiene 2 posibles estados verdadero o falso
```python
x = True
y : bool = False
```
### Cadenas
Una cadena es una secuencia de caracteres
```python
x = "cadena"
y : str = "string"
```

# Operadores
Los operadores hacen una acción dependiendo de su tipo y regresan un valor
## Operadores binarios
Son operadores que toman dos variables/valores
### Operadores Aritméticos
```python
x = 1 + 2   # regresa la suma
x = 1 - 2   # regresa la resta
x = 1 * 2   # regresa la multiplicacion
x = 1 / 2   # regresa la division (0.5 un float)
x = 1 // 2  # regresa la division entera (0 un int)
x = 1 % 2   # regresa la remanente
x = - 2     # regresa la negacion
```

### Operadores Lógicos 
Estos tipos de operadores esperan que les pases un tipo booleano.
Si estos reciben cualquier otro tipo regresaran uno de los valores de acuerdo a cual de los dos fue evaluado al final
```python
True and False  # Regresa True si los dos son verdadero 
True or False   # Regresa True si uno de los dos es verdadero
not False       # Regresa el opuesto
```

Cuando se evalua un `x and y` estos se convierte en `bool(x) and bool(y)` luego, si `bool(x)` es verdadero se evalua `bool(y)` y se regresa `y` si `bool(x)` es falso se regresara `x`

Cuando se evalua un `x or y` estos se convierte en `bool(x) or bool(y)` luego, si `bool(x)` es falso se evalua `bool(y)` y se regresa `y` si `bool(x)` es verdadero se regresara `x`

Cuando se evalua `not x` se convierte en `not bool(x)` y si `bool(x)` es verdadero regresa `False` y si `bool(x)` es falso regresa `True`

```python
1.0 and 2.0     # => True and True => 2.0
0.0 and 2.0     # => False and True => 0.0
1.0 or 2.0      # => True or True => 1.0
0.0 or 2.0      # => False or True => 2.0
not 0.0         # => not False => True
not 1.0         # => not True => False
```

### Operadores Comparativos
Son los operados utilizados para comparar dos variables / valores
regresan un valor booleano
```python
1 == 2          # Es igual
1 <= 2          # Es menor o igual que
1 >= 2          # Es mayor o igual que
1 < 2           # Es menor que
1 > 2           # Es mayor que
1 != 2          # Es diferente que
1 is int        # Es del tipo
1 is not int    # No es del tipo
```

## Asignación modificación
Hace una operación sobre una variable y la asigna hacia la variable
```python
x += 2      # Asignacion Suma            Equivalente: x = x + 2
x -= 2      # Asignacion Resta           Equivalente: x = x - 2
x *= 2      # Asignacion Multiplicacion  Equivalente: x = x * 2
x /= 2      # Asignacion Division        Equivalente: x = x / 2
x //= 2     # Asignacion Division entera Equivalente: x // x + 2
x %= 2      # Asignacion Remanente       Equivalente: x = x % 2
```

# Interacción con el usuario
## leer de la terminal
```python
x = input("...")         # leer una cadena
y = int(input("..."))    # leer un numero entero
z = float(input("..."))  # leer un numero decimal
```

## escribir a la terminal
```python
print(x)        # escribir variable
print('texto')  # escribir valor str
print(2)        # escribir valor int
print(2,x,3)    # escribir varias cosas
```
