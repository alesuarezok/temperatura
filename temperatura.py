# El siguiente programa debe poder clasificar la temperatura segun el siguiente criterio
# como temparatura maxima 53
# y como minimo -40 en grados celcius
#(si pasa el maximo o esta por debajo del minimo, Respondera el mensaje "Entrada invalida")
"""__________________________________________
            |                                |
temperatura | denominacion                   |
____________|________________________________|
            |		                         |
  temp < 0  | "Sensacion del clima Helado"   |
____________|________________________________|
            |                                |
0<= temp <15|  "Sensacion del clima Frio"    |    
____________|________________________________|            
            |                                |
15<=temp<25 | "Sensacion del clima gradable" |
____________|________________________________|            
            |                                |
temp >= 25  |  "Sensacion del clima caluroso"|
____________|________________________________|"""

# definicion
def observar_clima():
    print ("Bienvenido")
    bandera = True  #hago una bandera para un bucle
    while (bandera == True): #hago un bucle para validar el input del usuario
        try:
            temperatura = int(input("Ingrese un valor: "))     # ingreso de valor
        except ValueError:     # carga de temperatura no es un número
            print ("No ingresaste un número!")
        else:
            if(temperatura < 0 and temperatura > -40): # -40 > temperatura < 0
                if (temperatura == 1): #singular para 1 grado
                    print ("Ingresaste", temperatura, "grado. Sensación del clima 'Helado', ¿de verdad tenes salir?")
                else:
                    print ("Ingresaste", temperatura, "grados. Sensación del clima 'Helado, ¿de verdad tenes salir?'")
                bandera = False
            # carga de valores entre 0 y 15
            elif (temperatura >= 0) and (temperatura < 15): # 0 <= temperatura < 15
                print ("Ingresaste", temperatura, "grados. Sensacion del clima 'Frio'. Está para bufanda y campera")
                bandera = False
            # carga de valores entre 15 y 25
            elif (temperatura >= 15) and (temperatura < 25): # 15 <= temperatura < 25
                print ("Ingresaste", temperatura, "grados. Sensacion del clima 'Agradable'. Ojalá que puedas disfrutar al aire libre")
                bandera = False
            # carga de valores entre 25 y 32
            elif (temperatura >= 25) and (temperatura < 32): # 25 <= temperatura < 32 
                print ("Ingresaste", temperatura, "grados. Sensacion del clima 'Caluroso'.")
                bandera = False
            # carga de valores entre 32 y temperatura maxima (53)
            elif (temperatura >= 32 and temperatura <= 53): # 32 <= temperatura
                print ("Ingresaste", temperatura, "grados. Sensacion del clima 'Muy caluroso, casi sofocante'. Si tenés que salir, ponete protector e hidratate mucho.")
                bandera = False
            else:
                print ("Intentalo nuevamente, las temperaturas ingresadas no son correctas")
                bandera = True #Ejecuto el bucle hasta que el user ingrese una temperatura menor a 53 y mayor a -40
    
observar_clima() # Permite que el programa inicie directamente
