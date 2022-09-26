"""Realizar un programa que conste de un clase Persona con dos atributos nombre y edad. Los atributos se introducirán por teclado y habrá otro método para imprimir los datos.

Declarar una segunda clase llama Empleado que hereda de la clase Persona y agrega el atributo sueldo. Debe mostrar si tiene que pagar impuestos o no (sueldo superior a 3000).

Crear un objeto de cada clase."""


# creamos la clase persona
class Persona:
    # creamos la primera funcion (método)
    # para inicializar el atributo (variable) nombre y edad
    def __init__(self):
        self.nombre=str(input("Ingrese su Nombre: "))
        self.edad=int(input("Ingrese su edad: "))


    # creamos el segundo metodo
    # para mostrar el nombre y edad
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)


# declaramos la clase empleado
# la clase empleado hereda los atributos y metodos de la clase Persona
class Empleado(Persona):
    # declaramos el metodo __init__
    def __init__(self):
        # llamamos al metodo init de la clase padre
        # utilizamos la funcion super() para hacer referencia al padre
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))

    # declaramos el metodo mostrar
    def mostrar(self):
        super().mostrar()
        print("Sueldo: ",self.sueldo)

    # declaramos el metodo pagar_impuestos
    # comprobara si el empleado debe pagar o no
    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos.")
        else:
            print("El empleado no paga impuestos.")
 
 
 
# bloque principal
#persona1=Persona()
#persona1.mostrar()
empleado1=Empleado()
empleado1.mostrar()
empleado1.pagar_impuestos()
