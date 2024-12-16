'''
Escribir una función que pida un número entero entre 1 y 10, lea el fichero 
tabla-n.txt con la tabla de multiplicar de ese número, donde n es el número 
introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar 
un mensaje por pantalla informando de ello.
'''

import os
n = int(input('Dame un numero del 1 al 10: '))
nombre = 'tabla.txt-' + str(n), 'w'
if os.path.isfile(nombre, 'w') == True:
    print('Ya existe un archivo con este nombre')
else:
    print('No existe ningun archivo con este nombre')

with open(nombre, 'w') as file:
    for i in range (1,11):
        file.write()
    n = n +1