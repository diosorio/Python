"""Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como atributos el nombre y la edad de una persona. 
Implementar los métodos necesarios para inicializar los atributos, mostrar los datos e indicar si la persona es mayor de edad o no."""


# creamos la clase Persona
class Persona:
    # creamos la primera funcion (método)
    # para inicializar el atributo (variable) nombre y edad
    def inicializar(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad


    # creamos el segundo metodo
    # para mostrar el nombre y edad
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)

    # creamos el tercer metodo
    # para mostrar si es mayor de edad o no
    def verificacion(self):
        if self.edad > 18:
            print("La persona es mayor.")
        else:
            print("No es mayor.")
 
 
 
# bloque principal
# creamos los nuevos objetos
individuo1=Persona()
individuo2=Persona()

# inicializamos los atributos
individuo1.inicializar("Maria",8)
individuo2.inicializar("Ramona",24)

# imprimimos los datos y resultados de cada persona
individuo1.mostrar()
individuo1.verificacion()
individuo2.mostrar()
individuo2.verificacion()
