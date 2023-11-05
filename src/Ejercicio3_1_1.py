'''
Ejercicio 3.1.1

Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla.
'''
def mostrarLista():
    lista =["Matematicas","Fisica","Quimica","Historia","Lengua"]
    return lista

def imprimirLista():
    asignaturas = mostrarLista()
    for asignatura in asignaturas:
        print(asignatura)
if __name__ == "__main__":

    imprimirLista()