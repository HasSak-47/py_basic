# Funciones
Una funcion es una pieza de codigo reutilizable, la cual puede tomar parametros y regresar un valor. esta puede ser llamada desde cualquier otra parte.
```python
def escriba_algo():
    x = int(input('escriba algo: '))
    return x

def lee_y_suma(y):
    x = escriba_algo()
    return x + y

print(lee_y_suma(10))
```
En este caso, se declararon 2 funciones `escriba_algo` y `lee_y_suma`, y se mando a llamar lee_y_suma con un valor de 10 en su parametro, el valor regresado por esta funcion luego es pasado a print.

La definicion de `escriba_algo` manda a llamar la funcion `input` con el valor `'escriba_algo'`en el parametro, lo guarda en x y regresa el valor de x. 

La definicion de `lee_y_suma` toma un valor y, manda a llamar `lee_y_suma` lo guarda en `x` y regresa la suma de `x + y`

# Salida y Regreso de valor
Para salir de una funcion se utiliza la keyword `return` esta puede ser acompañada por una variable o valor, lo que hara es que la funcion regrese un valor, en lugar de nada.

si se quiere que una funcion regrese nada, no se tiene que especificar return al final de su scope.

```python
def foo():
    bar = int(input('escriba: '))
    if bar == 10:
        return 'exelente'
    elif bar == 0:
        return -1
    diff = 10 - bar
    for i in range(diff):
        print(i)
```

en este caso la funcion `foo` no toma ningun parametro, lee un numero de la terminal y lo guarda en `bar`, checa si es 10, si es 10, regresa `'exelente'`, si es 0 regresa `-1` y si es ninguno de los dos, guarda `10 - bar` end `diff` luego itera desde 0 a `diff` imprimendo los valores. regresando nada
