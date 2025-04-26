
# Verifica si una cadena es un número hexadecimal válido.Permite signo negativo al principio y acepta letras en mayúscula.
def es_hexagonal(numero_str):
    if not numero_str:
        return False
    if numero_str[0] == '-':
        numero_str = numero_str[1:]
    return all(c in '0123456789ABCDEF' for c in numero_str)

#Convierte un carácter hexadecimal individual a su valor decimal.Acepta letras mayúsculas y minúsculas (A-F, a-f).
def hexa_a_decimal(caracter):
    if caracter == '0':
        return 0
    elif caracter == '1':
        return 1
    elif caracter == '2':
        return 2
    elif caracter == '3':
        return 3
    elif caracter == '4':
        return 4
    elif caracter == '5':
        return 5
    elif caracter == '6':
        return 6
    elif caracter == '7':
        return 7
    elif caracter == '8':
        return 8
    elif caracter == '9':
        return 9
    elif caracter == 'A' or caracter == 'a':
        return 10
    elif caracter == 'B' or caracter == 'b':
        return 11
    elif caracter == 'C' or caracter == 'c':
        return 12
    elif caracter == 'D' or caracter == 'd':
        return 13
    elif caracter == 'E' or caracter == 'e':
        return 14
    elif caracter == 'F' or caracter == 'f':
        return 15
    else:
        return False

#Convierte una cadena hexadecimal completa a su valor decimal.Recorre el número de derecha a izquierda, multiplicando cada dígito por 16^posición.
def conver_hexa_deci(numeroHexa):
    i = len(numeroHexa) - 1
    j = 0
    decimal_total = 0
    while i >= 0:
        numerodeci = hexa_a_decimal(numeroHexa[i])
        decimal_total = decimal_total + numerodeci * (16 ** j)
        i -= 1
        j += 1
    return decimal_total

 #Convierte un número decimal a su representación binaria en forma de cadena.Usa divisiones sucesivas por 2.
def conver_hexa_bin(decimal_total):
    dividendo = decimal_total
    num_binario = ''
    while dividendo > 0:
        residuo = dividendo % 2
        num_binario = str(residuo) + num_binario
        dividendo = dividendo // 2
    return num_binario if num_binario else '0'

#Convierte un número decimal a su representación octal en forma de cadena.Usa divisiones sucesivas por 8.
def conver_hexa_octal(decimal_total):
    dividendo = decimal_total
    num_octal = ''
    while dividendo > 0:
        residuo = dividendo % 8
        num_octal = str(residuo) + num_octal
        dividendo = dividendo // 8
    return num_octal if num_octal else '0'


