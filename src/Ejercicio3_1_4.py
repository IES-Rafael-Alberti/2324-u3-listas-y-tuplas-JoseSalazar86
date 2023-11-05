'''
Ejercicio 3.1.4

Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''

def listaPrimitiva():
    numerosPrimitiva = []
    return numerosPrimitiva

def leerEntradaLista():
    numeros = listaPrimitiva()
    for i in range(6):
        numero = int(input(f"Introduce el número {i+1} de la primitiva ganador: "))
        numeros.append(numero)
    return numeros

def ordenarNumerosPrimitiva():
    numeros = leerEntradaLista()
    numeros.sort()
    mostrarMensaje(numeros)

def mostrarMensaje(numeros):
    print("Los números ganadores de la lotería primitiva ordenados de menor a mayor son:")
    for numero in numeros:
        print(numero)

if __name__ == "__main__":
    ordenarNumerosPrimitiva()

