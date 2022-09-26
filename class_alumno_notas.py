"""Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""



# creamos la clase alumno
class Alumno:
    # creamos la primera funcion (método)
    # para inicializar el atributo (variable) nombre y nota
    def __init__(self):
        self.nombre=str(input("Ingrese Nombre del Alumno: "))
        self.nota=float(input("Ingrese Nota del Alumno: "))


    # creamos el segundo metodo
    # para mostrar el nombre y nota
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)

    # creamos el tercer metodo
    # para mostrar si ha aprobado o no
    def curso(self):
        if self.nota > 8:
            print("El Alumno aprobó el curso.")
        else:
            print("El alumno reprobó el curso.")
 
 
 
# bloque principal
alumno1=Alumno()
alumno1.mostrar()
alumno1.curso()

alumno2=Alumno()
alumno2.mostrar()
alumno2.curso()

alumno3=Alumno()
alumno3.mostrar()
alumno3.curso()
