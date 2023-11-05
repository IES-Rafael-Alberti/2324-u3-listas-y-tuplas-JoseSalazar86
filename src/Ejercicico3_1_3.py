'''
Ejercicio 3.1.3

Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
y después las muestre por pantalla con el mensaje En <asignatura> has sacado 
<nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota>
cada una de las correspondientes notas introducidas por el usuario.
'''
def listaAsignatura():
    asignatura = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
    return asignatura

def leeEntrada(asignaturas):
    notas = []
    for asignatura in asignaturas:
        nota = input(f"Introduce las notas de {asignatura}: ")
        notas.append(nota)
    return notas

def mostrarMensaje(asignaturas,nota):
    for i in range(len(asignaturas)):
        print(f"\nEn {asignaturas[i]} has sacado {nota[i]}.")

if __name__ == "__main__":
    asignaturas = listaAsignatura()
    notas = leeEntrada(asignaturas)
    mostrarMensaje(asignaturas, notas)


