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


# Muestra el Resultado de la Conversión
print(f"\nEl Número Binario {binario_original} convertido a Decimal es {nro_decimal}")


"""
Binario a Octal
"""

# Se copia el Nro Decimal del Ejercicio anterior a la Variable decimal_octal para trabajar con ella
decimal_octal = nro_decimal

# Se crea una variable y se inicializa vacía No en 0 porque usará string posteriormente
nro_octal = ""

# Mientras el Nro Decimal sea Mayor a 0 continua el ciclo
# 1º Se extrae el resto del número que divimos por 8
# 2º Al Nro Octal se le suma el Resto (en String) y se le agrega el nro Octal que arrastre
# 3º Al Nro Octal se le quita el resto

while decimal_octal > 0:
    resto = decimal_octal % 8
    nro_octal = str(resto) + nro_octal
    decimal_octal = decimal_octal // 8

# Muestra el Resultado de la Conversión
print(f"El Número Binario {binario_original} convertido a Octal es {nro_octal}")



"""
Binario a Hexadecimal
"""

# Crea una Variable que indica la letra que le corresponde a cada Número en el Sistema Hexadecimal
valores_hexa = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

# Se copia el Nro Decimal del 1º Ejercicio a la Variable decimal_hexa para trabajar con ella
decimal_hexa = nro_decimal

# Se crea una variable y se inicializa vacía No en 0 porque usará string posteriormente
nro_hexa = ""


# Mientras el Nro Decimal sea Mayor a 0 continua el ciclo
# 1º Se extrae el resto del número que divimos por 16
# 2º Preguntamos si el resto es menor a 10 y si es Verdadero operamos igual que el ejercicio anterior. (paso 3º)
# 3º Al Nro Hexadecimal se le suma el Resto (en String) y se le agrega el nro Hexadecimal que arrastre.
# 4º Sino, si el resto es Mayor o Igual a 10 entonces tomamos el valor alfabético que le corresponde al número decimal y se le agrega el nro Hexadecimal que arrastre.
# 5º Al Nro Hexadecimal se le quita el resto

while decimal_hexa > 0:
    resto = decimal_hexa % 16
    if resto < 10:
        nro_hexa = str(resto) + nro_hexa
    else:
        nro_hexa = valores_hexa[resto] + nro_hexa
    decimal_hexa = decimal_hexa // 16


# Muestra el Resultado de la Conversión
print(f"El Número Binario {binario_original} convertido a Hexadecimal es {nro_hexa}")