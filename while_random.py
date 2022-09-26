import random #importo librería random, para elegir nros al azar

while True:

    resultado_1 = random.randint(1,15) 
    resultado_2 = random.randint(1,15)
    total = resultado_1 + resultado_2 #guardo en variable total, los dos valores del dado. Para imprimir la suma
    print ("Los 2 números obtenidos son: " , resultado_1, "y" , resultado_2)
    print ("La suma de los 2 números es: ", total)
    repetir = input ("Presione la tecla q si desea salir u otra si quiere lanzar nuevamente: ") 
    if repetir == 'q':
        break
#El ciclo while se repite, si se recibe la entrada de una tecla diferente de "q" al finalizar
