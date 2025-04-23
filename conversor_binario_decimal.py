print("\n*******************************************************")
print("*  Conversor Binario a Decimal, Octal y Hexadecimal   *")
print("*******************************************************\n")


# Ingreso del número binario
nro_binario = input("Ingresá un número binario (solo 0 y 1): ")


# Verifica si el número es binario
nro_es_binario = True
for digito in nro_binario :
    if digito != '0' and digito != '1' :
        nro_es_binario = False
        break

# Mientras el Nro No sea Binario seguirá pidiendo que ingrese el nro
while nro_es_binario == False :
    print("\n* CUIDADO! El Nro Ingresado NO es un Nro Binario\n")
    nro_binario = input("Ingresá un número binario (solo 0 y 1): ")

    # Aquí repito el código de verificación pero dentro del Ciclo
    nro_es_binario = True
    for digito in nro_binario :
        if digito != '0' and digito != '1' :
            nro_es_binario = False
            break


# Convierte el Nro Ingresado como Cadena a un Nro Entero
nro_binario = int(nro_binario)

# Se guarda el binario original
binario_original = nro_binario

"""
Binario a Decimal
"""
# Se inicializa en 0 el Nro. Decimal y la Potencia

nro_decimal = 0
potencia = 0

# Mientras el binario sea Mayor a 0 continua el ciclo
# 1º Se extrae el resto
# 2º Al Nro Decimal se le suma el Resto multiplicado por la base elevado a la potencia correspondiente
# 3º A la Potencia le sumo 1 para el siguiente cálculo
# 4º Al Nro Binario le quito el resto

while nro_binario > 0:

    resto = nro_binario % 10
    nro_decimal = nro_decimal + resto * (2 ** potencia)
    potencia += 1
    nro_binario = nro_binario // 10

print(f"\nEl Número Binario {binario_original} convertido a Decimal es {nro_decimal}")


"""
Binario a Decimal
"""







"""


# Paso 2: Decimal a Octal
octal = 0
multiplicador = 1
temp = decimal
while temp > 0:
    resto = temp % 8
    octal += resto * multiplicador
    multiplicador *= 10
    temp //= 8

print("Octal:", octal)

# Paso 3: Decimal a Hexadecimal
hex_map = "0123456789ABCDEF"
hexadecimal = ""
temp = decimal
while temp > 0:
    resto = temp % 16
    hexadecimal = hex_map[resto] + hexadecimal
    temp //= 16

if hexadecimal == "":
    hexadecimal = "0"

print("Hexadecimal:", hexadecimal)


"""
