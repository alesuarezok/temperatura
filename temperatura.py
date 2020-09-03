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

# ingreso de valor
    temperatura=int(input("Ingrese un valor: "))
# carga de temperatura invalida
    if(temperatura < -40) or (temperatura > 53):
		respuesta = "Entrada invalida"
# temperatura entre los valores -40 y 0
    elif(temperatura < 0): # -40 > temperatura < 0
		respuesta = "Sensacion del clima 'Helado'"
# carga de valores entre 0 y 15
    elif (temperatura >= 0) and (temperatura < 15): # 0 <= temperatura < 15  
	    respuesta = "Sensacion del clima 'Frio'"
# carga de valores entre 15 y 25
    elif (temperatura >= 15) and (temperatura < 25): # 15 <= temperatura < 25
	    respuesta = "Sensacion del clima 'Agradable'"
