#creamos el diccionario
tabla = {'Jhon': 4127, 'Jack': 4098, 'Dany': 7678}

#recorremos el diccionario
for nombre, telefono in tabla.items():
    print('{0:10} ==> {1:10d}'.format(nombre, telefono)) #formateamos la salida
