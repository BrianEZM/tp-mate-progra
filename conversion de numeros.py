#input
numero=int(input("Ingrese un numero entero:"))

opcion=0


#conversion de decimal a binario
binario=""
while numero > 0:
        if numero %2 == 0:
           binario ="0" + binario
        else:   
           binario ="1" + binario
        
        numero= numero // 2

print(f"El numero ingresado a binario es:{binario}")
        
#conversion de binario a decimal
            
decimal= 0
posicion= len(binario)
for i in reversed(binario):
        if i == "1":
           decimal= decimal + pow(2, (len(binario)) - posicion)
        posicion -= 1
        
print(f"El numero ingresado a decimal es:{decimal}")
                        
        












