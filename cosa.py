#!/bin/python
from subprocess import Popen, PIPE
from os import getcwd


# Lee todo de un archivo y lo regresa
def read_all(path: str):
    s = ""
    with open(path) as file:
        for line in file.readlines():
            print(line)
            s += line

    return s


def main():
    # archivos que este programa correra
    codes = ['codigo2.py', 'codigo3.py', 'codigo4.py', 'codigo5.py']
    inputs = []
    # carga los inputs que le dara a los codigos
    with open('sequences.txt') as f:
        inputs = f.readlines()
    # convierte los inputs de str a bytes
    inputs = [bytes(input, 'utf-8') for input in inputs]

    # ejecuta los programas
    for code, input in zip(codes, inputs):
        # imprime el nombre del programa
        print(f'sh-5.1$ python {code}')
        print(input.decode()[:-2])

        # lanza el programa
        args = ['python', code] # los argumentos necesarios para abrir un programa
        p = Popen(args, stdout=PIPE, stdin=PIPE, stderr=PIPE, cwd=getcwd()) # abre el programa
        stdout_data = p.communicate(input)[0]  # le manda informacion al codigo

        print(stdout_data.decode()) # imprime el resultado
    return 0


# guardia para asegurarse que no corra si no es el archivo principal
if __name__ == '__main__':
    main()
