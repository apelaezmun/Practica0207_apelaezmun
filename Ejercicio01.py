'''
Escribir una función que pida un número entero entre 1 y 10 y guarde en un 
fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, 
donde n es el número introducido.
'''

n = int(input('Dame un numero del 1 al 10: '))
nombre = 'tabla-' + str(n) + '.txt'
with open(nombre, 'w') as file:
    for i in range(1, 11):
        file.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')