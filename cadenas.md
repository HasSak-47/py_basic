# Creacion de cadena
La cadena es una secuencia de caracteres, la manera en la que funciona es que es una lista de numeros, y cada simbolo le pertenece a un numero.
Por ejemplo la letra `A` tiene el valor `65`

Las cadenas pueden ser creadas usando `'` o `"`
```python
cadena = 'esto es una cadena'
cadena = "esto es tambien es una cadena"
```
## Formas de crear cadenas
hay 4 formas de crear cadenas de acuerdo si necesites que sean varias lineas o una sola al momento de escribirlas en el codigo fuente, o al momento de imprimirlas
```python
a = 'esto es una cadena de una linea'
b = 'esta es una \
cadena de una linea \
rota en varias'
c = '''esto es una cadena
de varias lineas
''' 
d = 'esto es una cadena\nde varias lineas en una sola'
```
cuando se imprimen estas cadenas queda de esta forma
```
esto es una cadena de una linea

esta es una cadena de una linea rota en varias

esto es una cadena
de varias lineas

esto es una cadena
de varias lineas en una sola
```

# Secuencia de escape
Las secuencias de escape se forman de la manera `\X` donde `X` es el valor escapado, estos pueden representar varias cosas

| SE | significado |
| - | - |
| `\n` | nueva linea |
| `\t` | tab |
| `\r` | regreso al inicio de linea |
| `\\` | Simbolo \ |
| `\'` | Simbolo ' |
| `\"` | Simbolo " |
| `\e` | valor 'esc' |
| `\xXX` | valor hex XX |
| `\0XX` | valor octal XX |

# Subcadenas
Una subcadena es una porcion de una cadena, esta se puede hacer de la forma `sub = cadena[a:b]` `sub` es una subcadena de `cadena` que contiene los caracteres desde `a` hasta `b` no incluida.

```python
cadena = 'test string'
sub = cadena[0:4]       # 'test' 
sub = cadena[:4]        # 'test' 
sub = cadena[0:-1]      # 'test strin' 
sub = cadena[:-1]       # 'test strin' 
sub = cadena[-6:]       # 'string' 
sub = cadena[5:]        # 'string' 
```
