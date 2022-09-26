# -*- coding: utf-8 -*-

class caja_registradora:

    def __init__(self, a=0, r=0, dinero_recibido=0, cambio=0, temp=0):

        print ("\n\n***** Bienvenido!!! *****\n")

        self.a = a
        self.r = r
        self.dinero_recibido = dinero_recibido
        self.cambio = cambio
        self.temp = temp


    def comida_rapida(self):
 
        print("***** Menú *****")
 
        print("1. Combo 1----->200", "\n2. Combo 2----->350", "\n3. Combo 3---->400", "\n4. Combo 4---->250", "\n5. Salir")
        print("\n")

        while (1):
 
            c = str(input("Seleccione: "))
 
            if (c == "1"):
                cantidad = int(input("Ingrese la cantidad: "))
                self.r = self.r + 200 * cantidad

                finalizar = input ("Presione la tecla f si desea finalizar sin seleccionar otro menú: ")
                print("\n")
                if (finalizar == 'f'):
                    print("total:", self.r)
                    cliente_plus = int(input("Presione 1 si es cliente plus, y 2 si no es: "))
                    dinero_recibido = int(input("Ingrese Dinero Recibido: "))
                    descuento = 5 * self.r / 100
                    
                    if(cliente_plus==1):
                        print("Cambio:",dinero_recibido - self.r + descuento)
                        print("\n\n")
                        print("*****Gracias por su preferencia!!!*****")
                        print("\n\n")
                    
                    if(cliente_plus==2):
                        print("Cambio:",dinero_recibido - self.r)
                        print("\n\n")
                        print("*****Gracias por su preferencia!!!*****")
                        print("\n\n")
                

            elif (c == "2"):
                cantidad = int(input("Ingrese la cantidad: "))
                self.r = self.r + 350 * cantidad

                finalizar = input ("Presione la tecla f si desea finalizar sin seleccionar otro menú: ")
                print("\n")
                if (finalizar == 'f'):
                    print("total:", self.r)
                    cliente_plus = int(input("Presione 1 si es cliente plus, y 2 si no es: "))
                    dinero_recibido = int(input("Ingrese Dinero Recibido: "))
                    descuento = 5 * self.r / 100
                    
                    if(cliente_plus==1):
                        print("Cambio:",dinero_recibido - self.r + descuento)
                        print("\n\n")
                        print("*****Gracias por su preferencia!!!*****")
                        print("\n\n")
                    
                    if(cliente_plus==2):
                        print("Cambio:",dinero_recibido - self.r)
                        print("\n\n")
                        print("*****Gracias por su preferencia!!!*****")
                        print("\n\n")

            elif (c == "3"):
                cantidad = int(input("Ingrese la cantidad: "))
                self.r = self.r + 400 * cantidad
            
                finalizar = input ("Presione la tecla f si desea finalizar sin seleccionar otro menú: ")
                print("\n")
                if (finalizar == 'f'):
                    print("total:", self.r)
                    cliente_plus = int(input("Presione 1 si es cliente plus, y 2 si no es: "))
                    dinero_recibido = int(input("Ingrese Dinero Recibido: "))
                    descuento = 5 * self.r / 100
                    
                    if(cliente_plus==1):
                        print("Cambio:",dinero_recibido - self.r + descuento)
                        print("\n\n")
                        print("*****Gracias por su preferencia!!!*****")
                        print("\n\n")

                    if(cliente_plus==2):
                        print("Cambio:",dinero_recibido - self.r)
                        print("\n\n")
                        print("*****Gracias por su preferencia!!!*****")
                        print("\n\n")

            elif (c == "4"):
                cantidad = int(input("Ingrese la cantidad: "))
                self.r = self.r + 250 * cantidad

                finalizar = input ("Presione la tecla f si desea finalizar sin seleccionar otro menú: ")
                print("\n")
                if (finalizar == 'f'):
                    print("total:", self.r)
                    cliente_plus = int(input("Presione 1 si es cliente plus, y 2 si no es: "))
                    dinero_recibido = int(input("Ingrese Dinero Recibido: "))
                    descuento = 5 * self.r / 100
                    
                    if(cliente_plus==1):
                        print("Cambio:",dinero_recibido - self.r + descuento)
                        print("\n\n")
                        print("*****Gracias por su preferencia!!!*****")
                        print("\n\n")

                    if(cliente_plus==2):
                        print("Cambio:",dinero_recibido - self.r)
                        print("\n\n")
                        print("***** Gracias por su preferencia!!! *****")
                        print("\n\n")

            elif (c == "5"):
                quit()

            
            else:
                print("\n\n")
                print("****** Opción Incorrecta ******")
                print("\n\n")
                
                
def main():
    a = caja_registradora()
 
    while (1):
 
            a.comida_rapida()

main()
