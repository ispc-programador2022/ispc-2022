#Escribir el código en Python que permita realizar lo siguiente:
#Crear una lista en Python denominada “Dueno” que contenga los siguientes valores:
# 28957346,  Juan,  Perez, 4789689,  Belgrano 101
# Dichos datos se corresponden  con los datos del dueño de un perro (DNI, nombre, apellido, teléfono y dirección). 
# Muestre en pantalla el teléfono del dueño si el DNI es mayor a 26000000.

Dueno=[28957346,  'Juan',  'Perez', 4789689,  'Belgrano 101'] #Creo la lista
indices={'DNI':0, 'nombre':1, 'apellido':2, 'telefono':3 ,'direccion':4} #Creo un diccionario para poder ubicar mejor los datos
if (Dueno[indices['DNI']])>26000000:
    print ("El telefono de "+Dueno[indices['nombre']]+" "+Dueno[indices['apellido']]+ " es "+str(Dueno[indices['telefono']]))
