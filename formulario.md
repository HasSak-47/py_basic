# Variables
## Tipos fuertes vs Tipos débiles
Un tipo debil puede tener cualquier tipo de valor
mientras que uno fuerte solo puede ser el que ya se le asigno
```python
x = 0        # Tipo debil
y : int = 0  # Tipo fuerte
```
## Creación y asignación
### Números enteros
Son todos los números enteros con infinita precision
```python
x = 0
y : int = 0  
```

## Modificar
```python
x = 1
y = 2
x = x + y   # ahora x vale el resultado de x + y es decir 3
x = 4       # ahora x vale 4
x = "test"  # Como x era un tipo debil ahora es una cadena

a : int = 1 
a = "test"  # error no puedes asignare a un int un str
```

### Números decimales/números reales
Es un tipo de número el cual representa un número decimal
estos no tienen una gran precision pero normalmente no importa
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
x = 1 + 2   # Suma
x = 1 - 2   # Resta
x = 1 * 2   # Multiplicacion
x = 1 / 2   # Division
x = 1 // 2  # Division entera
x = 1 % 2   # Remanente
```

### Operadores Lógicos 
```python
x = True and False  # Regresa True si los dos son verdadero 
x = True or False   # Regresa True si uno de los dos es verdadero
```

### Operadores Comparativos
Son los operados utilizados para comparar dos variables / valores
regresan un valor booleano
```python
x = 1 == 2          # Es igual
x = 1 <= 2          # Es menor o igual que
x = 1 >= 2          # Es mayor o igual que
x = 1 < 2           # Es menor que
x = 1 > 2           # Es mayor que
x = 1 != 2          # Es diferente que
x = 1 is int        # Es del tipo
x = 1 is not int    # No es del tipo
```

## Operadores unarios
Son operadores que toman solo una variable
### Operadores Aritméticos
```python
x = - 2     # negacion
```

### Operadores Lógicos 
```python
x = not False   # Regresa el opuesto 
```

## Asignación modificación
Hace una operación sobre una variable y la asigna hacia la variable
```python
x += 2      # Asignacion Suma            Equivalente: x = x + 2
x -= 2      # Asignacion Resta           Equivalente: x = x - 2
x *= 2      # Asignacion Multiplicacion  Equivalente: x = x * 2
x /= 2      # Asignacion Division        Equivalente: x = x / 2
x //= 2     # Asignacion Division entera Equivalente: x // x + 
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
```
